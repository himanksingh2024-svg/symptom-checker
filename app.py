import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("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"))

st.title("AI Symptom Checker")

symptoms = st.text_area("Describe your symptoms...")
analyze = st.button("Analyze")

if symptoms and analyze:
    with st.spinner("Analyzing your symptoms..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a medical assistant AI. When a user provides symptoms, return the possible disease, explanation, warnings, diet plan, and precautions. Always include a disclaimer."},
                {"role": "user", "content": symptoms}
            ]
        )
        result = response.choices[0].message.content
    st.write(result)