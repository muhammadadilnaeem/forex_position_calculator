

---

# 🧮 Forex Position Size Calculator (Python + Streamlit)

## 📌 What the App Will Calculate

The calculator will determine **lot size based on risk management**.

### Inputs

1️⃣ Account Balance
2️⃣ Risk % per trade
3️⃣ Stop Loss (pips)
4️⃣ Pair Type

* Forex pair
* XAUUSD (Gold)

### Formula Used

$$
\text{Position Size} =
\frac{\text{Account Balance} \times \text{Risk %}}
{\text{Stop Loss (pips)} \times \text{Pip Value}}
$$

For **XAUUSD**

* **1 Standard Lot = 100 oz**
* **1 Pip = 0.01**
* **Pip value = $1 per lot**

---

# 📂 Project Structure

```
forex_position_calculator/
│
├── app.py
├── style.css
└── requirements.txt
```

---

# 📦 requirements.txt

```txt
streamlit
```

Install:

```bash
pip install -r requirements.txt
```

---

# 🎨 CSS for Professional UI

Create **style.css**

```css
.main-title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#FFD700;
}

.card {
    padding:30px;
    border-radius:15px;
    background-color:#1e1e1e;
    box-shadow:0px 0px 15px rgba(0,0,0,0.4);
}

.result-box {
    padding:20px;
    border-radius:10px;
    background-color:#0f5132;
    color:white;
    font-size:24px;
    text-align:center;
}
```

---

# 🐍 Streamlit App Code

Create **app.py**

```python
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
```

---

# ▶️ Run the App

```bash
streamlit run app.py
```

---

# 💻 App UI Features

Your app will include:

✅ Clean **trading dashboard style**
✅ Risk management calculator
✅ XAUUSD support (missing in many tools)
✅ Professional CSS cards
✅ Responsive layout

---

