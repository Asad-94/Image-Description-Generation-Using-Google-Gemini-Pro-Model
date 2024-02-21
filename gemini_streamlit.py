#!/usr/bin/env python
# coding: utf-8


# In[5]:


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


# In[2]:


os.environ['GOOGLE_API_KEY'] = "Enter your API key"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


# In[3]:


# Function to load Gemini model

model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(text, image):
    if text != "":
        response = model.generate_content([text, image])
    else:
        response = model.generate_content(image)
    return response.text


# In[4]:


# Initializing streamlit app

st.set_page_config(page_title= "Gemini Pro Vision Demo")
st.header("Gemini Application")
text = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Generate")

# When submit is clicked

if submit:
    response=get_gemini_response(text, image)
    st.write(response)


# In[ ]:




