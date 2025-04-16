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

# Custom CSS for dark theme styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #FFFFFF;
    }
    .main {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(255,255,255,0.05);
    }
    .stTextArea > label {
        font-size: 18px;
        color: #ffffff;
    }
    .stButton button {
        background-color: #00adb5;
        color: #ffffff;
        font-weight: bold;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        margin-top: 12px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #00ced1;
    }
    </style>
""", unsafe_allow_html=True)

# Main app container
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff;'>📩 SMS Spam Detection App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bbbbbb;'>🔍 Enter your SMS message below to find out if it's <strong>SPAM</strong> or <strong>HAM</strong>.</p>", unsafe_allow_html=True)

# Input area
msg = st.text_area("✉️ Your message:")

# Prediction
if st.button("🔎 Classify Message"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message first!")
    else:
        vec = vectorizer.transform([msg])
        pred = model.predict(vec)[0]
        if pred == 1:
            st.markdown("<h3 style='color: #ff4c4c; text-align: center;'>🚫 This is SPAM!</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color: #00ff99; text-align: center;'>✅ This is HAM (safe)</h3>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
