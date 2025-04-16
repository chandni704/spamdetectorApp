# Trigger rebuild

import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Page config
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
    }
    .stTextArea > label {
        font-size: 18px;
    }
    .stButton button {
        background-color: #6f42c1;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>📩 SMS Spam Detection App</h1>", unsafe_allow_html=True)
st.write("🔍 Enter an SMS message below and find out whether it's **spam** or **ham**!")

# Input area
msg = st.text_area("✉️ Your message:")

# Prediction
if st.button("🔎 Classify Message"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message first!")
    else:
        vec = vectorizer.transform([msg])
        pred = model.predict(vec)[0]
        result = "🚫 This is *SPAM!*" if pred == 1 else "✅ This is *HAM* (safe)"
        color = "red" if pred == 1 else "green"
        st.markdown(f"<h3 style='color:{color}; text-align:center;'>{result}</h3>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
