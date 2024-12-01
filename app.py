import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.title(":red[Text Summarizer]")
st.write("Application to summarize text using LLM")

text = st.text_area("Enter text to summarize:", height=200)

if st.button("Summarize", icon="✍🏼",use_container_width=True):
    with st.spinner("Summarizing..."):
        response = model.generate_content(f"Summarize the text: {text}")
    st.write("Summary:")
    st.write(response.text)