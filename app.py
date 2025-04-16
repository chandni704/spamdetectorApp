# Trigger rebuild

import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Title
st.title("📩 SMS Spam Detection App")

# User Input
msg = st.text_area("Enter your message here:")

if st.button("Classify"):
    if msg.strip() == "":
        st.warning("Please enter a message.")
    else:
        vec = vectorizer.transform([msg])
        pred = model.predict(vec)[0]
        result = "🚫 Spam" if pred == 1 else "✅ Ham"
        st.success(f"Prediction: {result}")
