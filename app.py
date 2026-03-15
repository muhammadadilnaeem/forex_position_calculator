import streamlit as st

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Gradient Heading
st.markdown("""
<style>
.main-title-box {
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    box-shadow: 0 6px 18px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.result-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #f0f2f6;
    font-weight: 600;
    font-size: 22px;
    text-align: center;
    margin-top: 20px;
}
</style>

<div class="main-title-box">
📊 Forex Position Size Calculator
</div>
""", unsafe_allow_html=True)

st.markdown("### Manage your risk like a professional trader")

# --- Inputs ---
pair_type = st.selectbox(
    "Select Instrument Type",
    options=["Forex Pair", "XAUUSD (Gold)", "Other"],
    index=1  # XAUUSD selected by default
)

balance = st.number_input("Account Balance ($)", value=1000, step=100)
risk_percent = st.slider("Risk % per Trade", 1, 10, 2)
stop_loss = st.number_input("Stop Loss (Pips)", value=50, step=1)

# --- Pip values ---
if pair_type == "Forex Pair":
    pip_value = 10
elif pair_type == "XAUUSD (Gold)":
    pip_value = 1  # Pip value for gold
else:
    pip_value = 1

# --- Calculate ---
if st.button("Calculate Position Size"):

    risk_amount = balance * (risk_percent / 100)
    lot_size = risk_amount / (stop_loss * pip_value)

    st.markdown(
        f"""
        <div class="result-box">
        Recommended Lot Size: {lot_size:.2f} lots
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("### Details")
    st.write(f"Risk Amount: ${risk_amount:.2f}")
    st.write(f"Pip Value: ${pip_value}")
