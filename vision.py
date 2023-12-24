from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model= genai.GenerativeModel(model_name="gemini-pro-vision")

#function to load gemini model to get responses
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ",key="input")

# Image upload
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""

if uploaded_image is not None:
    st.success("Image uploaded successfully!")
    # Display the uploaded image
    st.subheader("Uploaded Image:")
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the image")   


if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
