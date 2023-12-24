from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model= genai.GenerativeModel(model_name="gemini-pro")

#function to load gemini model to get responses
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
   

#initialize streamlit

st.set_page_config(page_title="Q&A App")

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask a Question")

## when submit id click

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
