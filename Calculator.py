import streamlit as st

# Set Page Config
st.set_page_config(page_title="Awesome Calculator", page_icon="🧮", layout="centered")

# Custom CSS for better visuals
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🧮 Awesome Calculator App")
st.subheader("Developed by Farzan Shah")
st.markdown("---")

# Input fields
st.markdown('<div class="main">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter First Number", format="%.2f", key="num1")
with col2:
    num2 = st.number_input("Enter Second Number", format="%.2f", key="num2")

operation = st.selectbox("Select Operation", ["➕ Addition", "➖ Subtraction", "✖️ Multiplication", "➗ Division", "🔢 Modulus", "🔼 Power"])

# Perform Calculation
result = None
if st.button("Calculate"):
    try:
        if operation == "➕ Addition":
            result = num1 + num2
        elif operation == "➖ Subtraction":
            result = num1 - num2
        elif operation == "✖️ Multiplication":
            result = num1 * num2
        elif operation == "➗ Division":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        elif operation == "🔢 Modulus":
            result = num1 % num2 if num2 != 0 else "Cannot find modulus with zero!"
        elif operation == "🔼 Power":
            result = num1 ** num2
    except Exception as e:
        result = f"Error: {e}"

    # Show Result
    st.success(f"✅ Result: {result}")

st.markdown("</div>", unsafe_allow_html=True)
