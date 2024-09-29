from dotenv import load_dotenv  #load environment variables from a .env file into the Python script
import os 
import google.generativeai as genai #interact with Google's generative AI models
import streamlit as st # framework for creating web apps 
from PIL import Image #library is used for opening, manipulating, and saving images
load_dotenv() #Loads environment variables from a .env file

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)  # Configures the Generative AI client with the API key retrieved from the environment variables.

def get_gemini_response(prompt,uploaded_image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # gemini-pro
    if prompt != "":   
        response = model.generate_content([prompt,uploaded_image])
    else:
        response = model.generate_content(uploaded_image)
    return response.text


st.set_page_config("gemini chatbot")
st.header("Chatbot Application using Gemini 🤖")
input = st.text_input("Input here : ",key='input')
uploaded_file = st.file_uploader("choose an image ...",type=['jpeg','jpg','png'])

image = ""
if uploaded_file is not None: 
    image = Image.open(uploaded_file)
    st.image(image,'uploaded image',use_column_width=True)  # image rendering on screen

# input , image    ==> llm model 

submit = st.button('SUBMIT')


if submit: 
    response = get_gemini_response(prompt=input,uploaded_image=image)
    st.subheader("Your response is :: ")
    st.write(response)


