import streamlit as st

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<p class="main-title">📊 Forex Position Size Calculator</p>', unsafe_allow_html=True)

st.markdown("### Manage your risk like a professional trader")

# Inputs
balance = st.number_input("Account Balance ($)", value=1000)

risk_percent = st.slider("Risk % per Trade", 1, 10, 2)

stop_loss = st.number_input("Stop Loss (Pips)", value=50)

pair_type = st.selectbox(
    "Select Instrument",
    ["Forex Pair", "XAUUSD (Gold)"]
)

# Pip values
if pair_type == "Forex Pair":
    pip_value = 10
else:
    pip_value = 1

# Calculate
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
