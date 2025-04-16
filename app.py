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
        background-color: #121212;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(255,255,255,0.1);
        color: white;
    }
    .stTextArea > label {
        font-size: 18px;
        color: white;
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

# Helper function to classify category
def get_category(message):
    msg = message.lower()
    if any(keyword in msg for keyword in ['otp', 'password', 'verification']):
        return "🔐 OTP / Security"
    elif any(keyword in msg for keyword in ['account', 'bank', 'credit', 'debit']):
        return "🏦 Banking"
    elif any(keyword in msg for keyword in ['sale', 'discount', 'offer', 'deal']):
        return "🛍️ Shopping / Offers"
    elif any(keyword in msg for keyword in ['friend', 'love', 'miss you']):
        return "💌 Personal"
    elif any(keyword in msg for keyword in ['win', 'prize', 'lottery']):
        return "🎁 Lottery / Prize"
    else:
        return "📄 General"

# Main UI
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>📩 SMS Spam Detection App</h1>", unsafe_allow_html=True)
st.write("🔍 Enter an SMS message below and find out whether it's **spam** or **ham**!")

msg = st.text_area("✉️ Your message:")

if st.button("🔎 Classify Message"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message first!")
    else:
        vec = vectorizer.transform([msg])
        pred = model.predict(vec)[0]
        result = "🚫 This is *SPAM!*" if pred == 1 else "✅ This is *HAM* (safe)"
        color = "red" if pred == 1 else "green"
        category = get_category(msg)

        st.markdown(f"<h3 style='color:{color}; text-align:center;'>{result}</h3>", unsafe_allow_html=True)
        st.markdown("### 📨 Your Message:")
        st.info(msg)
        st.markdown(f"### 🏷️ Category: **{category}**")

st.markdown("</div>", unsafe_allow_html=True)
