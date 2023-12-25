from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model 

model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_geimini_response(question):
    response = chat.send_message(question,stream=True)
    return response


st.set_page_config(page_title="chat App")

st.header("Gemini LLM Application")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input:",key="input")
submit = st.button("Ask Question")

if submit and input:
    response = get_geimini_response(input)
    st.session_state["chat_history"].append(("You",input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("AI",chunk.text))


# Display the chat history in the sidebar
st.sidebar.header("Chat History")  

for sender,text in st.session_state["chat_history"]:
    st.sidebar.text(f"{sender}:{text}")

