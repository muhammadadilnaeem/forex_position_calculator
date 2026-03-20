

import streamlit as st
import textwrap

def html(raw: str):
    """Render HTML — strips leading indent so Streamlit never treats it as a code block."""
    st.markdown(textwrap.dedent(raw).strip(), unsafe_allow_html=True)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="XAUUSD Position Calculator",
    page_icon="🥇",
    layout="centered",
)

# ── CSS — Risk Pro Navy/Gold Theme ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

/* ── CSS Variables (Risk Pro palette) ── */
:root {
    --navy-900:      #060D1F;
    --navy-800:      #0A1628;
    --navy-700:      #0D1F3C;
    --gold:          #D4AF37;
    --gold-light:    #FFE082;
    --gold-dim:      #FFD54F;
    --blue-accent:   #82B1FF;
    --green-accent:  #69F0AE;
    --red-accent:    #FF8A80;
    --text-primary:  #E8EAF0;
    --text-secondary:#8899AA;
    --text-muted:    #566A80;
    --glass-bg:      rgba(13, 31, 60, 0.7);
    --glass-border:  rgba(212, 175, 55, 0.12);
    --card-shadow:   0 8px 32px rgba(0,0,0,0.45), 0 1px 0 rgba(212,175,55,0.07) inset;
}

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    background-color: var(--navy-900) !important;
    color: var(--text-primary) !important;
    font-family: 'Poppins', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 2rem 1.5rem 4rem !important;
    max-width: 780px !important;
}

/* ── App background (Risk Pro mesh) ── */
.stApp {
    background: radial-gradient(ellipse at 20% 0%, #0D1F3C 0%, #060D1F 50%, #060D1F 100%);
    background-attachment: fixed;
}
body::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(212,175,55,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(212,175,55,0.025) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
}

/* ── Header ── */
.header-wrap {
    text-align: center;
    padding: 48px 24px 36px;
    margin-bottom: 4px;
}
.header-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(212,175,55,0.08);
    border: 1px solid rgba(212,175,55,0.22);
    border-radius: 999px;
    padding: 5px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 20px;
}
.header-chip::before {
    content: '';
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--gold);
    box-shadow: 0 0 8px var(--gold);
    animation: pulse 2s ease infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
}
.header-title {
    font-family: 'Poppins', sans-serif;
    font-size: clamp(32px, 7vw, 52px);
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.1;
    background: linear-gradient(90deg, var(--gold) 0%, var(--gold-light) 50%, var(--gold) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.header-sub {
    font-family: 'Poppins', sans-serif;
    font-size: 13px;
    font-weight: 400;
    color: var(--text-secondary);
    margin-top: 10px;
    letter-spacing: 0.4px;
}

/* ── Card container ── */
.calc-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 32px 28px;
    position: relative;
    box-shadow: var(--card-shadow);
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    overflow: hidden;
}
.calc-card::before {
    content: '';
    position: absolute;
    top: 0; left: 20px; right: 20px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.5), transparent);
}

/* ── Section labels (Risk Pro style) ── */
.section-label {
    font-family: 'Poppins', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--gold);
    border-left: 3px solid var(--gold);
    padding-left: 0.75rem;
    margin: 0 0 1rem 0;
    display: block;
}

/* ── Streamlit widget overrides ── */
.stSelectbox label,
.stNumberInput label,
.stSlider label {
    font-family: 'Poppins', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    color: var(--text-secondary) !important;
    text-transform: uppercase !important;
}

.stSelectbox > div > div {
    background: rgba(212,175,55,0.05) !important;
    border: 1px solid rgba(212,175,55,0.2) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}
.stSelectbox > div > div:hover {
    border-color: rgba(212,175,55,0.5) !important;
}
.stSelectbox svg { color: var(--gold) !important; }

.stNumberInput > div > div > input {
    background: rgba(212,175,55,0.05) !important;
    border: 1px solid rgba(212,175,55,0.2) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 20px !important;
    font-weight: 500 !important;
    text-align: center !important;
}
.stNumberInput > div > div > input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(212,175,55,0.1) !important;
}
.stNumberInput button {
    background: rgba(212,175,55,0.06) !important;
    border: 1px solid rgba(212,175,55,0.18) !important;
    color: var(--gold) !important;
    border-radius: 8px !important;
}
.stNumberInput button:hover {
    background: rgba(212,175,55,0.15) !important;
}

/* Slider — gold track */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, var(--gold), var(--gold-light)) !important;
}
.stSlider > div > div > div > div > div {
    background: #ffffff !important;
    border: 2px solid var(--gold) !important;
    box-shadow: 0 0 12px rgba(212,175,55,0.55) !important;
    width: 18px !important;
    height: 18px !important;
}
[data-baseweb="slider"] [role="slider"] { background: var(--gold) !important; }
.stSlider .st-bq { background: rgba(212,175,55,0.1) !important; }

/* ── Risk badge ── */
.risk-badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 32px;
    font-weight: 700;
    color: var(--gold-dim);
    background: rgba(212,175,55,0.07);
    border: 1px solid rgba(212,175,55,0.22);
    border-radius: 12px;
    padding: 6px 20px;
    letter-spacing: 1px;
    text-align: center;
    min-width: 90px;
}
.risk-label {
    font-family: 'Poppins', sans-serif;
    font-size: 11px;
    font-weight: 500;
    color: var(--text-muted);
    letter-spacing: 0.08em;
    text-align: center;
    margin-top: 6px;
}

/* ── Calculate button ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #1a3a6e 0%, #D4AF37 100%) !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 15px 32px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 24px rgba(212,175,55,0.25), 0 1px 0 rgba(255,255,255,0.08) inset !important;
    margin-top: 8px !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(212,175,55,0.4), 0 1px 0 rgba(255,255,255,0.12) inset !important;
    background: linear-gradient(135deg, #1a3a6e 0%, #FFE082 100%) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Result card ── */
.result-outer {
    background: linear-gradient(135deg, rgba(212,175,55,0.08), rgba(6,13,31,0.95));
    border: 1px solid rgba(212,175,55,0.22);
    border-radius: 20px;
    padding: 36px 28px 32px;
    position: relative;
    box-shadow: var(--card-shadow), 0 0 60px rgba(212,175,55,0.06);
    margin-top: 8px;
    animation: fadeSlideUp 0.35s cubic-bezier(0.22,1,0.36,1);
    backdrop-filter: blur(12px);
    overflow: hidden;
}
.result-outer::before {
    content: '';
    position: absolute;
    top: 0; left: 20px; right: 20px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}

.lot-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 5px;
    color: var(--text-muted);
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.lot-value {
    font-family: 'Space Mono', monospace;
    font-size: clamp(64px, 15vw, 108px);
    font-weight: 700;
    line-height: 1;
    text-align: center;
    background: linear-gradient(135deg, #ffffff 0%, var(--gold) 55%, var(--gold-dim) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 28px rgba(212,175,55,0.3));
    letter-spacing: -2px;
}
.lot-unit {
    font-family: 'Poppins', sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 5px;
    color: var(--text-secondary);
    text-align: center;
    text-transform: uppercase;
    margin-top: 4px;
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
    gap: 8px;
    flex-wrap: wrap;
}
.stat-item {
    text-align: center;
    flex: 1;
    min-width: 90px;
    background: rgba(212,175,55,0.04);
    border: 1px solid rgba(212,175,55,0.09);
    border-radius: 12px;
    padding: 12px 8px;
}
.stat-val {
    font-family: 'Space Mono', monospace;
    font-size: 17px;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: 0;
}
.stat-lbl {
    font-family: 'Poppins', sans-serif;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-top: 5px;
}

/* Warning strip */
.warning-strip {
    background: rgba(212,175,55,0.05);
    border: 1px solid rgba(212,175,55,0.14);
    border-left: 3px solid var(--gold);
    border-radius: 10px;
    padding: 12px 16px;
    margin-top: 20px;
    font-family: 'Poppins', sans-serif;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 0.2px;
    color: var(--text-muted);
    line-height: 1.7;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 44px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--text-muted);
    opacity: 0.4;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
html("""
<div class="header-wrap">
    <div class="header-chip">&#9679; Live Risk Engine</div>
    <div class="header-title">Position Calculator</div>
    <div class="header-sub">XAU/USD &middot; Forex &middot; Commodities &mdash; Professional Risk Management</div>
</div>
""")

# ── Inputs Card ───────────────────────────────────────────────────────────────
html('<div class="calc-card">')
html('<span class="section-label">01 &middot; Instrument</span>')

pair_type = st.selectbox(
    "Select Instrument Type",
    options=["XAUUSD (Gold)", "Forex Pair", "Other"],
    index=0,
)

html('<span class="section-label" style="margin-top:24px;">02 &middot; Account Parameters</span>')

col1, col2 = st.columns(2)
with col1:
    balance = st.number_input("Account Balance (USD)", value=10000, step=500, min_value=100)
with col2:
    stop_loss = st.number_input("Stop Loss (Pips)", value=50, step=1, min_value=1)

html('<span class="section-label" style="margin-top:24px;">03 &middot; Risk Exposure</span>')

risk_percent = st.slider("Risk % per Trade", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

# Live risk preview
risk_dollar_preview = balance * (risk_percent / 100)
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_b:
    html(f"""
<div style="text-align:center; margin: 8px 0 4px;">
    <div class="risk-badge">{risk_percent:.1f}%</div>
    <div class="risk-label">approx ${risk_dollar_preview:,.0f} at risk</div>
</div>
""")

html("</div>")  # close calc-card

# ── Calculate Button ──────────────────────────────────────────────────────────
_, col_btn, _ = st.columns([0.5, 3, 0.5])
with col_btn:
    calculate = st.button("⚡  Calculate Position Size")

# ── Results ───────────────────────────────────────────────────────────────────
if calculate:
    pip_value_map = {
        "Forex Pair":    10.0,
        "XAUUSD (Gold)":  1.0,
        "Other":          1.0,
    }
    pip_value = pip_value_map[pair_type]

    risk_amount = balance * (risk_percent / 100)
    lot_size    = risk_amount / (stop_loss * pip_value)
    pip_cost    = pip_value * lot_size

    # Risk tier — Risk Pro color palette
    if risk_percent <= 2:
        risk_color = "#69F0AE"   # green
        risk_tier  = "CONSERVATIVE"
    elif risk_percent <= 4:
        risk_color = "#FFD54F"   # gold
        risk_tier  = "MODERATE"
    else:
        risk_color = "#FF8A80"   # red
        risk_tier  = "AGGRESSIVE"

    result_html = (
        '<div class="result-outer">'
        '<div class="lot-label">Recommended Lot Size</div>'
        f'<div class="lot-value">{lot_size:.2f}</div>'
        '<div class="lot-unit">Standard Lots</div>'
        '<div class="stats-divider"></div>'
        '<div class="stats-row">'
        f'<div class="stat-item"><div class="stat-val" style="color:#FFD54F;">${risk_amount:,.2f}</div><div class="stat-lbl">Capital at Risk</div></div>'
        f'<div class="stat-item"><div class="stat-val" style="color:#82B1FF;">${pip_value:.2f}</div><div class="stat-lbl">Pip Value / Lot</div></div>'
        f'<div class="stat-item"><div class="stat-val" style="color:{risk_color};">{risk_tier}</div><div class="stat-lbl">Risk Profile</div></div>'
        f'<div class="stat-item"><div class="stat-val" style="color:#E8EAF0;">{stop_loss} pips</div><div class="stat-lbl">Stop Loss</div></div>'
        '</div>'
        '<div class="warning-strip">'
        '&#9888;&nbsp; RISK DISCLOSURE &mdash; Trading leveraged instruments carries significant risk. '
        'Position sizes are calculated based on your defined risk parameters only. '
        'Past performance does not guarantee future results. Trade responsibly.'
        '</div>'
        '</div>'
    )
    st.markdown(result_html, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
html('<div class="footer">XAU/USD Position Calculator &middot; Professional Risk Engine &middot; v2.0</div>')

# # Deep blue/navy professional
# import streamlit as st
# import textwrap

# def html(raw: str):
#     """Render HTML — strips leading indent so Streamlit never treats it as a code block."""
#     st.markdown(textwrap.dedent(raw).strip(), unsafe_allow_html=True)

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="XAUUSD Position Calculator",
#     page_icon="⚡",
#     layout="centered",
# )

# # ── All CSS injected inline ───────────────────────────────────────────────────
# st.markdown("""
# <style>
# /* ── Google Fonts ── */
# @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&family=Syne:wght@700;800&display=swap');

# /* ── CSS Variables ── */
# :root {
#     --navy-900: #050d1a;
#     --navy-800: #081428;
#     --navy-700: #0d1f3c;
#     --navy-600: #122a52;
#     --navy-500: #1a3a6e;
#     --cyan:     #00d4ff;
#     --cyan-dim: #0099bb;
#     --blue-mid: #3b82f6;
#     --text-primary: #e8f0fe;
#     --text-secondary: #7a9cc8;
#     --text-muted: #3a5a80;
#     --glass-bg: rgba(13, 31, 60, 0.7);
#     --glass-border: rgba(0, 212, 255, 0.12);
#     --card-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 1px 0 rgba(0,212,255,0.08) inset;
# }

# /* ── Reset & Base ── */
# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body, [class*="css"] {
#     background-color: var(--navy-900) !important;
#     color: var(--text-primary) !important;
#     font-family: 'DM Sans', sans-serif !important;
# }

# /* Hide Streamlit chrome */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container {
#     padding: 2rem 1.5rem 4rem !important;
#     max-width: 800px !important;
# }

# /* ── Mesh background ── */
# body::before {
#     content: '';
#     position: fixed;
#     inset: 0;
#     background:
#         radial-gradient(ellipse 80% 60% at 50% -10%, rgba(0,100,255,0.18) 0%, transparent 70%),
#         radial-gradient(ellipse 40% 40% at 90% 80%, rgba(0,212,255,0.08) 0%, transparent 60%);
#     pointer-events: none;
#     z-index: 0;
# }
# body::after {
#     content: '';
#     position: fixed;
#     inset: 0;
#     background-image:
#         linear-gradient(rgba(0,212,255,0.025) 1px, transparent 1px),
#         linear-gradient(90deg, rgba(0,212,255,0.025) 1px, transparent 1px);
#     background-size: 48px 48px;
#     pointer-events: none;
#     z-index: 0;
# }

# /* ── Header ── */
# .header-wrap {
#     text-align: center;
#     padding: 52px 24px 40px;
#     margin-bottom: 4px;
# }
# .header-chip {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     background: rgba(0,212,255,0.08);
#     border: 1px solid rgba(0,212,255,0.2);
#     border-radius: 999px;
#     padding: 5px 14px;
#     font-family: 'DM Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 3px;
#     color: var(--cyan);
#     text-transform: uppercase;
#     margin-bottom: 20px;
# }
# .header-chip::before {
#     content: '';
#     width: 6px; height: 6px;
#     border-radius: 50%;
#     background: var(--cyan);
#     box-shadow: 0 0 8px var(--cyan);
#     animation: pulse 2s ease infinite;
# }
# @keyframes pulse {
#     0%, 100% { opacity: 1; }
#     50%       { opacity: 0.3; }
# }
# .header-title {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(42px, 9vw, 76px);
#     font-weight: 800;
#     letter-spacing: -1px;
#     line-height: 1;
#     color: var(--text-primary);
# }
# .header-title span {
#     background: linear-gradient(90deg, var(--cyan) 0%, var(--blue-mid) 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
# }
# .header-sub {
#     font-family: 'DM Sans', sans-serif;
#     font-size: 14px;
#     font-weight: 400;
#     color: var(--text-secondary);
#     margin-top: 12px;
#     letter-spacing: 0.5px;
# }

# /* ── Card container ── */
# .calc-card {
#     background: var(--glass-bg);
#     border: 1px solid var(--glass-border);
#     border-radius: 20px;
#     padding: 32px 28px;
#     position: relative;
#     box-shadow: var(--card-shadow);
#     margin-bottom: 20px;
#     backdrop-filter: blur(12px);
#     -webkit-backdrop-filter: blur(12px);
#     overflow: hidden;
# }
# .calc-card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 20px; right: 20px;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(0,212,255,0.5), transparent);
# }

# /* ── Section labels ── */
# .section-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 4px;
#     color: var(--text-muted);
#     text-transform: uppercase;
#     margin-bottom: 16px;
#     display: flex;
#     align-items: center;
#     gap: 10px;
# }
# .section-label::after {
#     content: '';
#     flex: 1;
#     height: 1px;
#     background: rgba(0,212,255,0.08);
# }

# /* ── Widget overrides ── */
# .stSelectbox label,
# .stNumberInput label,
# .stSlider label {
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 12px !important;
#     font-weight: 600 !important;
#     letter-spacing: 1.5px !important;
#     color: var(--text-secondary) !important;
#     text-transform: uppercase !important;
# }

# .stSelectbox > div > div {
#     background: rgba(5, 13, 26, 0.8) !important;
#     border: 1px solid rgba(0,212,255,0.15) !important;
#     border-radius: 12px !important;
#     color: var(--text-primary) !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 15px !important;
#     font-weight: 500 !important;
# }
# .stSelectbox > div > div:hover {
#     border-color: rgba(0,212,255,0.4) !important;
# }
# .stSelectbox svg { color: var(--cyan) !important; }

# .stNumberInput > div > div > input {
#     background: rgba(5, 13, 26, 0.8) !important;
#     border: 1px solid rgba(0,212,255,0.15) !important;
#     border-radius: 12px !important;
#     color: var(--text-primary) !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 20px !important;
#     font-weight: 500 !important;
#     text-align: center !important;
# }
# .stNumberInput > div > div > input:focus {
#     border-color: var(--cyan) !important;
#     box-shadow: 0 0 0 3px rgba(0,212,255,0.1) !important;
# }
# .stNumberInput button {
#     background: rgba(0,212,255,0.06) !important;
#     border: 1px solid rgba(0,212,255,0.15) !important;
#     color: var(--cyan) !important;
#     border-radius: 8px !important;
# }
# .stNumberInput button:hover {
#     background: rgba(0,212,255,0.15) !important;
# }

# /* Slider */
# .stSlider > div > div > div > div {
#     background: linear-gradient(90deg, var(--blue-mid), var(--cyan)) !important;
# }
# .stSlider > div > div > div > div > div {
#     background: #ffffff !important;
#     border: 2px solid var(--cyan) !important;
#     box-shadow: 0 0 12px rgba(0,212,255,0.5) !important;
#     width: 18px !important;
#     height: 18px !important;
# }
# [data-baseweb="slider"] [role="slider"] {
#     background: var(--cyan) !important;
# }
# .stSlider .st-bq { background: rgba(0,212,255,0.1) !important; }

# /* ── Risk badge ── */
# .risk-badge {
#     display: inline-block;
#     font-family: 'DM Mono', monospace;
#     font-size: 34px;
#     font-weight: 500;
#     color: var(--cyan);
#     background: rgba(0,212,255,0.07);
#     border: 1px solid rgba(0,212,255,0.2);
#     border-radius: 14px;
#     padding: 6px 20px;
#     letter-spacing: 1px;
#     text-align: center;
#     min-width: 90px;
# }
# .risk-label {
#     font-family: 'DM Sans', sans-serif;
#     font-size: 11px;
#     font-weight: 500;
#     color: var(--text-muted);
#     letter-spacing: 1px;
#     text-align: center;
#     margin-top: 6px;
# }

# /* ── Button ── */
# .stButton > button {
#     width: 100% !important;
#     background: linear-gradient(135deg, #1a56db 0%, #00b4d8 100%) !important;
#     color: #ffffff !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 16px !important;
#     font-weight: 700 !important;
#     letter-spacing: 1px !important;
#     border: none !important;
#     border-radius: 14px !important;
#     padding: 16px 32px !important;
#     cursor: pointer !important;
#     transition: all 0.2s ease !important;
#     box-shadow: 0 4px 24px rgba(0,180,216,0.35), 0 1px 0 rgba(255,255,255,0.1) inset !important;
#     margin-top: 8px !important;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 32px rgba(0,180,216,0.5), 0 1px 0 rgba(255,255,255,0.15) inset !important;
#     background: linear-gradient(135deg, #2563eb 0%, #00d4ff 100%) !important;
# }
# .stButton > button:active { transform: translateY(0) !important; }

# /* ── Result card ── */
# .result-outer {
#     background: var(--glass-bg);
#     border: 1px solid rgba(0,212,255,0.2);
#     border-radius: 20px;
#     padding: 36px 28px 32px;
#     position: relative;
#     box-shadow: var(--card-shadow), 0 0 60px rgba(0,100,255,0.08);
#     margin-top: 8px;
#     animation: fadeSlideUp 0.35s cubic-bezier(0.22,1,0.36,1);
#     backdrop-filter: blur(12px);
#     overflow: hidden;
# }
# .result-outer::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 20px; right: 20px;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, var(--cyan), transparent);
# }
# @keyframes fadeSlideUp {
#     from { opacity: 0; transform: translateY(24px); }
#     to   { opacity: 1; transform: translateY(0); }
# }

# .lot-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 5px;
#     color: var(--text-muted);
#     text-align: center;
#     text-transform: uppercase;
#     margin-bottom: 4px;
# }
# .lot-value {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(68px, 16vw, 112px);
#     font-weight: 800;
#     line-height: 1;
#     text-align: center;
#     background: linear-gradient(135deg, #ffffff 0%, var(--cyan) 60%, var(--blue-mid) 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     filter: drop-shadow(0 0 28px rgba(0,212,255,0.3));
#     letter-spacing: -2px;
# }
# .lot-unit {
#     font-family: 'DM Sans', sans-serif;
#     font-size: 13px;
#     font-weight: 500;
#     letter-spacing: 4px;
#     color: var(--text-secondary);
#     text-align: center;
#     text-transform: uppercase;
#     margin-top: 2px;
# }

# /* Stats row */
# .stats-divider {
#     width: 100%;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(0,212,255,0.15), transparent);
#     margin: 24px 0;
# }
# .stats-row {
#     display: flex;
#     justify-content: space-around;
#     gap: 8px;
#     flex-wrap: wrap;
# }
# .stat-item {
#     text-align: center;
#     flex: 1;
#     min-width: 90px;
#     background: rgba(0,212,255,0.04);
#     border: 1px solid rgba(0,212,255,0.08);
#     border-radius: 12px;
#     padding: 12px 8px;
# }
# .stat-val {
#     font-family: 'DM Mono', monospace;
#     font-size: 18px;
#     font-weight: 500;
#     color: var(--text-primary);
#     letter-spacing: 0;
# }
# .stat-lbl {
#     font-family: 'DM Sans', sans-serif;
#     font-size: 10px;
#     font-weight: 600;
#     letter-spacing: 1.5px;
#     color: var(--text-muted);
#     text-transform: uppercase;
#     margin-top: 5px;
# }

# /* Warning strip */
# .warning-strip {
#     background: rgba(59,130,246,0.06);
#     border: 1px solid rgba(59,130,246,0.15);
#     border-left: 3px solid var(--blue-mid);
#     border-radius: 10px;
#     padding: 12px 16px;
#     margin-top: 20px;
#     font-family: 'DM Sans', sans-serif;
#     font-size: 11px;
#     font-weight: 400;
#     letter-spacing: 0.2px;
#     color: var(--text-muted);
#     line-height: 1.7;
# }

# /* Footer */
# .footer {
#     text-align: center;
#     margin-top: 44px;
#     font-family: 'DM Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 3px;
#     color: var(--text-muted);
#     opacity: 0.4;
#     text-transform: uppercase;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── Header ────────────────────────────────────────────────────────────────────
# html("""
# <div class="header-wrap">
# <div class="header-chip">&#9679; Live Risk Engine</div>
# <div class="header-title">Position <span>Calculator</span></div>
# <div class="header-sub">XAU/USD &middot; Forex &middot; Commodities &mdash; Professional Risk Management</div>
# </div>
# """)

# # ── Inputs Card ───────────────────────────────────────────────────────────────
# html('<div class="calc-card">')
# html('<div class="section-label">01 &middot; Instrument</div>')

# pair_type = st.selectbox(
#     "Select Instrument Type",
#     options=["XAUUSD (Gold)", "Forex Pair", "Other"],
#     index=0,
# )

# html('<div class="section-label" style="margin-top:24px;">02 &middot; Account Parameters</div>')

# col1, col2 = st.columns(2)
# with col1:
#     balance = st.number_input("Account Balance (USD)", value=10000, step=500, min_value=100)
# with col2:
#     stop_loss = st.number_input("Stop Loss (Pips)", value=50, step=1, min_value=1)

# html('<div class="section-label" style="margin-top:24px;">03 &middot; Risk Exposure</div>')

# risk_percent = st.slider("Risk % per Trade", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

# # Live risk preview
# risk_dollar_preview = balance * (risk_percent / 100)
# col_a, col_b, col_c = st.columns([1, 1, 1])
# with col_b:
#     html(f"""
# <div style="text-align:center; margin: 8px 0 4px;">
# <div class="risk-badge">{risk_percent:.1f}%</div>
# <div class="risk-label">approx ${risk_dollar_preview:,.0f} at risk</div>
# </div>
# """)

# html("</div>")

# # ── Calculate Button ──────────────────────────────────────────────────────────
# _, col_btn, _ = st.columns([0.5, 3, 0.5])
# with col_btn:
#     calculate = st.button("⚡  Calculate Position Size")

# # ── Results ───────────────────────────────────────────────────────────────────
# if calculate:
#     # Pip values
#     pip_value_map = {
#         "Forex Pair": 10.0,
#         "XAUUSD (Gold)": 1.0,
#         "Other": 1.0,
#     }
#     pip_value = pip_value_map[pair_type]

#     risk_amount   = balance * (risk_percent / 100)
#     lot_size      = risk_amount / (stop_loss * pip_value)
#     units         = lot_size * 100_000 if pair_type == "Forex Pair" else lot_size * 100
#     risk_reward   = risk_amount
#     pip_cost      = pip_value * lot_size

#     # Risk tier colour
#     risk_color = (
#         "#00d4ff" if risk_percent <= 2 else
#         "#f59e0b" if risk_percent <= 4 else
#         "#ef4444"
#     )
#     risk_tier = (
#         "CONSERVATIVE" if risk_percent <= 2 else
#         "MODERATE" if risk_percent <= 4 else
#         "AGGRESSIVE"
#     )

#     result_html = (
#         '<div class="result-outer">'
#         '<div class="lot-label">Recommended Lot Size</div>'
#         f'<div class="lot-value">{lot_size:.2f}</div>'
#         '<div class="lot-unit">Standard Lots</div>'
#         '<div class="stats-divider"></div>'
#         '<div class="stats-row">'
#         f'<div class="stat-item"><div class="stat-val" style="color:#00d4ff;">${risk_amount:,.2f}</div><div class="stat-lbl">Capital at Risk</div></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:#e8f0fe;">${pip_value}</div><div class="stat-lbl">Pip Value / Lot</div></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:{risk_color};">{risk_tier}</div><div class="stat-lbl">Risk Profile</div></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:#e8f0fe;">{stop_loss} pips</div><div class="stat-lbl">Stop Loss</div></div>'
#         '</div>'
#         '<div class="warning-strip">'
#         '&#9888;&nbsp; RISK DISCLOSURE &mdash; Trading leveraged instruments carries significant risk. '
#         'Position sizes are calculated based on your defined risk parameters only. '
#         'Past performance does not guarantee future results. Trade responsibly.'
#         '</div>'
#         '</div>'
#     )
#     st.markdown(result_html, unsafe_allow_html=True)

# # ── Footer ────────────────────────────────────────────────────────────────────
# html('<div class="footer">XAU/USD Position Calculator &middot; Professional Risk Engine &middot; v2.0</div>')


#-----------
# Balck And Golden

# import streamlit as st
# import textwrap

# def html(raw: str):
#     """Render HTML — strips leading indent so Streamlit never treats it as a code block."""
#     st.markdown(textwrap.dedent(raw).strip(), unsafe_allow_html=True)

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="XAUUSD Position Calculator",
#     page_icon="⚡",
#     layout="centered",
# )

# # ── All CSS injected inline ───────────────────────────────────────────────────
# st.markdown("""
# <style>
# /* ── Google Fonts ── */
# @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');

# /* ── Reset & Base ── */
# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body, [class*="css"] {
#     background-color: #080808 !important;
#     color: #e8d5a0 !important;
#     font-family: 'Rajdhani', sans-serif !important;
# }

# /* Hide Streamlit chrome */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container {
#     padding: 2rem 1.5rem 4rem !important;
#     max-width: 780px !important;
# }

# /* ── Animated background grid ── */
# body::before {
#     content: '';
#     position: fixed;
#     inset: 0;
#     background-image:
#         linear-gradient(rgba(212,175,55,0.04) 1px, transparent 1px),
#         linear-gradient(90deg, rgba(212,175,55,0.04) 1px, transparent 1px);
#     background-size: 40px 40px;
#     pointer-events: none;
#     z-index: 0;
# }

# /* ── Header ── */
# .header-wrap {
#     position: relative;
#     text-align: center;
#     padding: 48px 24px 36px;
#     margin-bottom: 8px;
# }
# .header-eyebrow {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 11px;
#     letter-spacing: 6px;
#     color: #d4af37;
#     opacity: 0.7;
#     text-transform: uppercase;
#     margin-bottom: 14px;
# }
# .header-title {
#     font-family: 'Bebas Neue', sans-serif;
#     font-size: clamp(52px, 10vw, 88px);
#     letter-spacing: 4px;
#     line-height: 0.95;
#     background: linear-gradient(135deg, #ffe066 0%, #d4af37 40%, #8b6914 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     filter: drop-shadow(0 0 32px rgba(212,175,55,0.35));
# }
# .header-sub {
#     font-family: 'Rajdhani', sans-serif;
#     font-size: 15px;
#     letter-spacing: 3px;
#     color: #a08828;
#     margin-top: 14px;
#     text-transform: uppercase;
# }
# .header-line {
#     width: 80px;
#     height: 2px;
#     background: linear-gradient(90deg, transparent, #d4af37, transparent);
#     margin: 20px auto 0;
# }

# /* ── Card container ── */
# .calc-card {
#     background: linear-gradient(145deg, #111009, #0d0d0d);
#     border: 1px solid rgba(212,175,55,0.18);
#     border-radius: 4px;
#     padding: 36px 32px;
#     position: relative;
#     box-shadow:
#         0 0 0 1px rgba(212,175,55,0.06),
#         0 24px 64px rgba(0,0,0,0.7),
#         inset 0 1px 0 rgba(212,175,55,0.12);
#     margin-bottom: 24px;
# }
# .calc-card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0; right: 0;
#     height: 2px;
#     background: linear-gradient(90deg, transparent 0%, #d4af37 30%, #ffe066 50%, #d4af37 70%, transparent 100%);
#     border-radius: 4px 4px 0 0;
# }

# /* ── Section labels ── */
# .section-label {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 5px;
#     color: #d4af37;
#     opacity: 0.55;
#     text-transform: uppercase;
#     margin-bottom: 20px;
#     display: flex;
#     align-items: center;
#     gap: 10px;
# }
# .section-label::after {
#     content: '';
#     flex: 1;
#     height: 1px;
#     background: rgba(212,175,55,0.15);
# }

# /* ── Streamlit widget overrides ── */
# /* Labels */
# .stSelectbox label,
# .stNumberInput label,
# .stSlider label {
#     font-family: 'Rajdhani', sans-serif !important;
#     font-size: 13px !important;
#     font-weight: 600 !important;
#     letter-spacing: 2px !important;
#     color: #a08828 !important;
#     text-transform: uppercase !important;
# }

# /* Select box */
# .stSelectbox > div > div {
#     background: #0a0900 !important;
#     border: 1px solid rgba(212,175,55,0.25) !important;
#     border-radius: 2px !important;
#     color: #e8d5a0 !important;
#     font-family: 'Rajdhani', sans-serif !important;
#     font-size: 16px !important;
#     font-weight: 600 !important;
# }
# .stSelectbox > div > div:hover {
#     border-color: rgba(212,175,55,0.6) !important;
# }
# .stSelectbox svg { color: #d4af37 !important; }

# /* Number inputs */
# .stNumberInput > div > div > input {
#     background: #0a0900 !important;
#     border: 1px solid rgba(212,175,55,0.25) !important;
#     border-radius: 2px !important;
#     color: #e8d5a0 !important;
#     font-family: 'Share Tech Mono', monospace !important;
#     font-size: 20px !important;
#     text-align: center !important;
# }
# .stNumberInput > div > div > input:focus {
#     border-color: #d4af37 !important;
#     box-shadow: 0 0 0 2px rgba(212,175,55,0.15) !important;
# }
# .stNumberInput button {
#     background: rgba(212,175,55,0.08) !important;
#     border: 1px solid rgba(212,175,55,0.2) !important;
#     color: #d4af37 !important;
# }
# .stNumberInput button:hover {
#     background: rgba(212,175,55,0.2) !important;
# }

# /* Slider */
# .stSlider > div > div > div > div {
#     background: linear-gradient(90deg, #d4af37, #ffe066) !important;
# }
# .stSlider > div > div > div > div > div {
#     background: #ffe066 !important;
#     border: 2px solid #080808 !important;
#     box-shadow: 0 0 10px rgba(212,175,55,0.6) !important;
#     width: 18px !important;
#     height: 18px !important;
# }
# [data-baseweb="slider"] [role="slider"] {
#     background: #ffe066 !important;
# }
# .stSlider .st-bq { background: rgba(212,175,55,0.15) !important; }

# /* ── Risk badge ── */
# .risk-badge {
#     display: inline-block;
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 32px;
#     font-weight: bold;
#     color: #ffe066;
#     background: rgba(212,175,55,0.08);
#     border: 1px solid rgba(212,175,55,0.3);
#     border-radius: 2px;
#     padding: 4px 16px;
#     letter-spacing: 2px;
#     text-align: center;
#     min-width: 80px;
# }
# .risk-label {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 10px;
#     color: #a08828;
#     letter-spacing: 4px;
#     text-transform: uppercase;
#     text-align: center;
#     margin-top: 4px;
# }

# /* ── Calculate button ── */
# .stButton > button {
#     width: 100% !important;
#     background: linear-gradient(135deg, #d4af37 0%, #ffe066 50%, #d4af37 100%) !important;
#     color: #080808 !important;
#     font-family: 'Bebas Neue', sans-serif !important;
#     font-size: 22px !important;
#     letter-spacing: 4px !important;
#     border: none !important;
#     border-radius: 2px !important;
#     padding: 14px 32px !important;
#     cursor: pointer !important;
#     transition: all 0.2s ease !important;
#     box-shadow: 0 0 24px rgba(212,175,55,0.25), 0 4px 16px rgba(0,0,0,0.4) !important;
#     margin-top: 8px !important;
#     text-transform: uppercase !important;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 0 40px rgba(212,175,55,0.45), 0 8px 24px rgba(0,0,0,0.5) !important;
#     background: linear-gradient(135deg, #ffe066 0%, #fff0a0 50%, #ffe066 100%) !important;
# }
# .stButton > button:active {
#     transform: translateY(0px) !important;
# }

# /* ── Result card ── */
# .result-outer {
#     background: linear-gradient(145deg, #0d0b00, #0f0e09);
#     border: 1px solid rgba(212,175,55,0.3);
#     border-radius: 4px;
#     padding: 36px 28px;
#     position: relative;
#     box-shadow:
#         0 0 40px rgba(212,175,55,0.08),
#         0 24px 64px rgba(0,0,0,0.6);
#     margin-top: 8px;
#     animation: fadeSlideUp 0.4s ease;
# }
# .result-outer::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0; right: 0;
#     height: 2px;
#     background: linear-gradient(90deg, transparent, #ffe066, #d4af37, #ffe066, transparent);
# }
# @keyframes fadeSlideUp {
#     from { opacity: 0; transform: translateY(20px); }
#     to   { opacity: 1; transform: translateY(0); }
# }

# .lot-label {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 11px;
#     letter-spacing: 6px;
#     color: #a08828;
#     text-align: center;
#     text-transform: uppercase;
#     margin-bottom: 6px;
# }
# .lot-value {
#     font-family: 'Bebas Neue', sans-serif;
#     font-size: clamp(64px, 16vw, 110px);
#     line-height: 1;
#     text-align: center;
#     background: linear-gradient(135deg, #ffe066 0%, #d4af37 50%, #8b6914 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     filter: drop-shadow(0 0 30px rgba(212,175,55,0.4));
#     letter-spacing: 2px;
# }
# .lot-unit {
#     font-family: 'Rajdhani', sans-serif;
#     font-size: 14px;
#     letter-spacing: 5px;
#     color: #a08828;
#     text-align: center;
#     text-transform: uppercase;
#     margin-top: -4px;
# }

# /* Stats row */
# .stats-divider {
#     width: 100%;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(212,175,55,0.2), transparent);
#     margin: 24px 0;
# }
# .stats-row {
#     display: flex;
#     justify-content: space-around;
#     gap: 12px;
#     flex-wrap: wrap;
# }
# .stat-item {
#     text-align: center;
#     flex: 1;
#     min-width: 100px;
# }
# .stat-val {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 22px;
#     color: #ffe066;
#     letter-spacing: 1px;
# }
# .stat-lbl {
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 9px;
#     letter-spacing: 3px;
#     color: #6b5510;
#     text-transform: uppercase;
#     margin-top: 4px;
# }
# .stat-divider {
#     width: 1px;
#     background: rgba(212,175,55,0.12);
#     align-self: stretch;
# }

# /* Warning strip */
# .warning-strip {
#     background: rgba(212,175,55,0.05);
#     border: 1px solid rgba(212,175,55,0.12);
#     border-left: 3px solid #d4af37;
#     border-radius: 2px;
#     padding: 10px 16px;
#     margin-top: 20px;
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 1px;
#     color: #7a6020;
#     line-height: 1.6;
# }

# /* Footer */
# .footer {
#     text-align: center;
#     margin-top: 40px;
#     font-family: 'Share Tech Mono', monospace;
#     font-size: 10px;
#     letter-spacing: 3px;
#     color: #2a2010;
#     text-transform: uppercase;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── Header ────────────────────────────────────────────────────────────────────
# html("""
# <div class="header-wrap">
# <div class="header-eyebrow">&#9889; Professional Risk Management</div>
# <div class="header-title">POSITION<br>CALCULATOR</div>
# <div class="header-sub">XAU/USD &middot; Forex &middot; Commodities</div>
# <div class="header-line"></div>
# </div>
# """)

# # ── Inputs Card ───────────────────────────────────────────────────────────────
# html('<div class="calc-card">')
# html('<div class="section-label">01 &middot; Instrument</div>')

# pair_type = st.selectbox(
#     "Select Instrument Type",
#     options=["XAUUSD (Gold)", "Forex Pair", "Other"],
#     index=0,
# )

# html('<div class="section-label" style="margin-top:24px;">02 &middot; Account Parameters</div>')

# col1, col2 = st.columns(2)
# with col1:
#     balance = st.number_input("Account Balance (USD)", value=10000, step=500, min_value=100)
# with col2:
#     stop_loss = st.number_input("Stop Loss (Pips)", value=50, step=1, min_value=1)

# html('<div class="section-label" style="margin-top:24px;">03 &middot; Risk Exposure</div>')

# risk_percent = st.slider("Risk % per Trade", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

# # Live risk preview
# risk_dollar_preview = balance * (risk_percent / 100)
# col_a, col_b, col_c = st.columns([1, 1, 1])
# with col_b:
#     html(f"""
# <div style="text-align:center; margin: 8px 0 4px;">
# <div class="risk-badge">{risk_percent:.1f}%</div>
# <div class="risk-label">approx ${risk_dollar_preview:,.0f} at risk</div>
# </div>
# """)

# html("</div>")

# # ── Calculate Button ──────────────────────────────────────────────────────────
# _, col_btn, _ = st.columns([0.5, 3, 0.5])
# with col_btn:
#     calculate = st.button("⚡  Calculate Position Size")

# # ── Results ───────────────────────────────────────────────────────────────────
# if calculate:
#     # Pip values
#     pip_value_map = {
#         "Forex Pair": 10.0,
#         "XAUUSD (Gold)": 1.0,
#         "Other": 1.0,
#     }
#     pip_value = pip_value_map[pair_type]

#     risk_amount   = balance * (risk_percent / 100)
#     lot_size      = risk_amount / (stop_loss * pip_value)
#     units         = lot_size * 100_000 if pair_type == "Forex Pair" else lot_size * 100
#     risk_reward   = risk_amount
#     pip_cost      = pip_value * lot_size

#     # Risk tier colour
#     risk_color = (
#         "#44ff88" if risk_percent <= 2 else
#         "#ffe066" if risk_percent <= 4 else
#         "#ff6644"
#     )
#     risk_tier = (
#         "CONSERVATIVE" if risk_percent <= 2 else
#         "MODERATE" if risk_percent <= 4 else
#         "AGGRESSIVE"
#     )

#     result_html = (
#         '<div class="result-outer">'
#         '<div class="lot-label">Recommended Lot Size</div>'
#         f'<div class="lot-value">{lot_size:.2f}</div>'
#         '<div class="lot-unit">Standard Lots</div>'
#         '<div class="stats-divider"></div>'
#         '<div class="stats-row">'
#         f'<div class="stat-item"><div class="stat-val" style="color:#e8d5a0;">${risk_amount:,.2f}</div><div class="stat-lbl">Capital at Risk</div></div>'
#         '<div class="stat-divider"></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:#e8d5a0;">${pip_value}</div><div class="stat-lbl">Pip Value / Lot</div></div>'
#         '<div class="stat-divider"></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:{risk_color};">{risk_tier}</div><div class="stat-lbl">Risk Profile</div></div>'
#         '<div class="stat-divider"></div>'
#         f'<div class="stat-item"><div class="stat-val" style="color:#e8d5a0;">{stop_loss} pips</div><div class="stat-lbl">Stop Loss</div></div>'
#         '</div>'
#         '<div class="warning-strip">'
#         '&#9888; RISK DISCLOSURE — Trading leveraged instruments carries significant risk. '
#         'Position sizes are calculated based on your defined risk parameters only. '
#         'Past performance does not guarantee future results. Trade responsibly.'
#         '</div>'
#         '</div>'
#     )
#     st.markdown(result_html, unsafe_allow_html=True)

# # ── Footer ────────────────────────────────────────────────────────────────────
# html('<div class="footer">XAU/USD Position Calculator &middot; Professional Risk Engine &middot; v2.0</div>')
