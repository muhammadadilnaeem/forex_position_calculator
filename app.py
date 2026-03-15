import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="XAUUSD Position Calculator",
    page_icon="⚡",
    layout="centered",
)

# ── All CSS injected inline ───────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    background-color: #080808 !important;
    color: #e8d5a0 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2rem 1.5rem 4rem !important;
    max-width: 780px !important;
}

/* ── Animated background grid ── */
body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(212,175,55,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(212,175,55,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
}

/* ── Header ── */
.header-wrap {
    position: relative;
    text-align: center;
    padding: 48px 24px 36px;
    margin-bottom: 8px;
}
.header-eyebrow {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 6px;
    color: #d4af37;
    opacity: 0.7;
    text-transform: uppercase;
    margin-bottom: 14px;
}
.header-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(52px, 10vw, 88px);
    letter-spacing: 4px;
    line-height: 0.95;
    background: linear-gradient(135deg, #ffe066 0%, #d4af37 40%, #8b6914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 32px rgba(212,175,55,0.35));
}
.header-sub {
    font-family: 'Rajdhani', sans-serif;
    font-size: 15px;
    letter-spacing: 3px;
    color: #a08828;
    margin-top: 14px;
    text-transform: uppercase;
}
.header-line {
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d4af37, transparent);
    margin: 20px auto 0;
}

/* ── Card container ── */
.calc-card {
    background: linear-gradient(145deg, #111009, #0d0d0d);
    border: 1px solid rgba(212,175,55,0.18);
    border-radius: 4px;
    padding: 36px 32px;
    position: relative;
    box-shadow:
        0 0 0 1px rgba(212,175,55,0.06),
        0 24px 64px rgba(0,0,0,0.7),
        inset 0 1px 0 rgba(212,175,55,0.12);
    margin-bottom: 24px;
}
.calc-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent 0%, #d4af37 30%, #ffe066 50%, #d4af37 70%, transparent 100%);
    border-radius: 4px 4px 0 0;
}

/* ── Section labels ── */
.section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 5px;
    color: #d4af37;
    opacity: 0.55;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(212,175,55,0.15);
}

/* ── Streamlit widget overrides ── */
/* Labels */
.stSelectbox label,
.stNumberInput label,
.stSlider label {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    color: #a08828 !important;
    text-transform: uppercase !important;
}

/* Select box */
.stSelectbox > div > div {
    background: #0a0900 !important;
    border: 1px solid rgba(212,175,55,0.25) !important;
    border-radius: 2px !important;
    color: #e8d5a0 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
.stSelectbox > div > div:hover {
    border-color: rgba(212,175,55,0.6) !important;
}
.stSelectbox svg { color: #d4af37 !important; }

/* Number inputs */
.stNumberInput > div > div > input {
    background: #0a0900 !important;
    border: 1px solid rgba(212,175,55,0.25) !important;
    border-radius: 2px !important;
    color: #e8d5a0 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 20px !important;
    text-align: center !important;
}
.stNumberInput > div > div > input:focus {
    border-color: #d4af37 !important;
    box-shadow: 0 0 0 2px rgba(212,175,55,0.15) !important;
}
.stNumberInput button {
    background: rgba(212,175,55,0.08) !important;
    border: 1px solid rgba(212,175,55,0.2) !important;
    color: #d4af37 !important;
}
.stNumberInput button:hover {
    background: rgba(212,175,55,0.2) !important;
}

/* Slider */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #d4af37, #ffe066) !important;
}
.stSlider > div > div > div > div > div {
    background: #ffe066 !important;
    border: 2px solid #080808 !important;
    box-shadow: 0 0 10px rgba(212,175,55,0.6) !important;
    width: 18px !important;
    height: 18px !important;
}
[data-baseweb="slider"] [role="slider"] {
    background: #ffe066 !important;
}
.stSlider .st-bq { background: rgba(212,175,55,0.15) !important; }

/* ── Risk badge ── */
.risk-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 32px;
    font-weight: bold;
    color: #ffe066;
    background: rgba(212,175,55,0.08);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 2px;
    padding: 4px 16px;
    letter-spacing: 2px;
    text-align: center;
    min-width: 80px;
}
.risk-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    color: #a08828;
    letter-spacing: 4px;
    text-transform: uppercase;
    text-align: center;
    margin-top: 4px;
}

/* ── Calculate button ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #d4af37 0%, #ffe066 50%, #d4af37 100%) !important;
    color: #080808 !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 22px !important;
    letter-spacing: 4px !important;
    border: none !important;
    border-radius: 2px !important;
    padding: 14px 32px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 0 24px rgba(212,175,55,0.25), 0 4px 16px rgba(0,0,0,0.4) !important;
    margin-top: 8px !important;
    text-transform: uppercase !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 40px rgba(212,175,55,0.45), 0 8px 24px rgba(0,0,0,0.5) !important;
    background: linear-gradient(135deg, #ffe066 0%, #fff0a0 50%, #ffe066 100%) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Result card ── */
.result-outer {
    background: linear-gradient(145deg, #0d0b00, #0f0e09);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 4px;
    padding: 36px 28px;
    position: relative;
    box-shadow:
        0 0 40px rgba(212,175,55,0.08),
        0 24px 64px rgba(0,0,0,0.6);
    margin-top: 8px;
    animation: fadeSlideUp 0.4s ease;
}
.result-outer::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #ffe066, #d4af37, #ffe066, transparent);
}
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.lot-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 6px;
    color: #a08828;
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.lot-value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(64px, 16vw, 110px);
    line-height: 1;
    text-align: center;
    background: linear-gradient(135deg, #ffe066 0%, #d4af37 50%, #8b6914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 30px rgba(212,175,55,0.4));
    letter-spacing: 2px;
}
.lot-unit {
    font-family: 'Rajdhani', sans-serif;
    font-size: 14px;
    letter-spacing: 5px;
    color: #a08828;
    text-align: center;
    text-transform: uppercase;
    margin-top: -4px;
}

/* Stats row */
.stats-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.2), transparent);
    margin: 24px 0;
}
.stats-row {
    display: flex;
    justify-content: space-around;
    gap: 12px;
    flex-wrap: wrap;
}
.stat-item {
    text-align: center;
    flex: 1;
    min-width: 100px;
}
.stat-val {
    font-family: 'Share Tech Mono', monospace;
    font-size: 22px;
    color: #ffe066;
    letter-spacing: 1px;
}
.stat-lbl {
    font-family: 'Share Tech Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    color: #6b5510;
    text-transform: uppercase;
    margin-top: 4px;
}
.stat-divider {
    width: 1px;
    background: rgba(212,175,55,0.12);
    align-self: stretch;
}

/* Warning strip */
.warning-strip {
    background: rgba(212,175,55,0.05);
    border: 1px solid rgba(212,175,55,0.12);
    border-left: 3px solid #d4af37;
    border-radius: 2px;
    padding: 10px 16px;
    margin-top: 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
    color: #7a6020;
    line-height: 1.6;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: #2a2010;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
    <div class="header-eyebrow">⚡ Professional Risk Management</div>
    <div class="header-title">POSITION<br>CALCULATOR</div>
    <div class="header-sub">XAU/USD · Forex · Commodities</div>
    <div class="header-line"></div>
</div>
""", unsafe_allow_html=True)

# ── Inputs Card ───────────────────────────────────────────────────────────────
st.markdown('<div class="calc-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">01 · Instrument</div>', unsafe_allow_html=True)

pair_type = st.selectbox(
    "Select Instrument Type",
    options=["XAUUSD (Gold)", "Forex Pair", "Other"],
    index=0,
)

st.markdown('<div class="section-label" style="margin-top:24px;">02 · Account Parameters</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    balance = st.number_input("Account Balance (USD)", value=10000, step=500, min_value=100)
with col2:
    stop_loss = st.number_input("Stop Loss (Pips)", value=50, step=1, min_value=1)

st.markdown('<div class="section-label" style="margin-top:24px;">03 · Risk Exposure</div>', unsafe_allow_html=True)

risk_percent = st.slider("Risk % per Trade", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

# Live risk preview
risk_dollar_preview = balance * (risk_percent / 100)
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_b:
    st.markdown(f"""
    <div style="text-align:center; margin: 8px 0 4px;">
        <div class="risk-badge">{risk_percent:.1f}%</div>
        <div class="risk-label">≈ ${risk_dollar_preview:,.0f} at risk</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Calculate Button ──────────────────────────────────────────────────────────
_, col_btn, _ = st.columns([0.5, 3, 0.5])
with col_btn:
    calculate = st.button("⚡  Calculate Position Size")

# ── Results ───────────────────────────────────────────────────────────────────
if calculate:
    # Pip values
    pip_value_map = {
        "Forex Pair": 10.0,
        "XAUUSD (Gold)": 1.0,
        "Other": 1.0,
    }
    pip_value = pip_value_map[pair_type]

    risk_amount   = balance * (risk_percent / 100)
    lot_size      = risk_amount / (stop_loss * pip_value)
    units         = lot_size * 100_000 if pair_type == "Forex Pair" else lot_size * 100
    risk_reward   = risk_amount
    pip_cost      = pip_value * lot_size

    # Risk tier colour
    risk_color = (
        "#44ff88" if risk_percent <= 2 else
        "#ffe066" if risk_percent <= 4 else
        "#ff6644"
    )
    risk_tier = (
        "CONSERVATIVE" if risk_percent <= 2 else
        "MODERATE" if risk_percent <= 4 else
        "AGGRESSIVE"
    )

    st.markdown(f"""
    <div class="result-outer">

        <div class="lot-label">Recommended Lot Size</div>
        <div class="lot-value">{lot_size:.2f}</div>
        <div class="lot-unit">Standard Lots</div>

        <div class="stats-divider"></div>

        <div class="stats-row">
            <div class="stat-item">
                <div class="stat-val" style="color:#e8d5a0;">${risk_amount:,.2f}</div>
                <div class="stat-lbl">Capital at Risk</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
                <div class="stat-val" style="color:#e8d5a0;">${pip_value}</div>
                <div class="stat-lbl">Pip Value / Lot</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
                <div class="stat-val" style="color:{risk_color};">{risk_tier}</div>
                <div class="stat-lbl">Risk Profile</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
                <div class="stat-val" style="color:#e8d5a0;">{stop_loss} pips</div>
                <div class="stat-lbl">Stop Loss</div>
            </div>
        </div>

        <div class="warning-strip">
            ⚠ &nbsp; RISK DISCLOSURE — Trading leveraged instruments carries significant risk. 
            Position sizes are calculated based on your defined risk parameters only. 
            Past performance does not guarantee future results. Trade responsibly.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    XAU/USD Position Calculator &nbsp;·&nbsp; Professional Risk Engine &nbsp;·&nbsp; v2.0
</div>
""", unsafe_allow_html=True)
