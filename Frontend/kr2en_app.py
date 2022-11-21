import streamlit as st
import requests

# Title and description
st.write("""
### Welcome to Korean 2 English Translator!
Let me help you translate!
"""
)

# search bar
input_text = st.text_input("Please insert a Korean text!")

if st.button('Translate'):
    payload = {
        "text": input_text
    }
    #output_text = requests.post(f"http://localhost:8000/translate", json = payload) # connects to backend/predict url locally.
    output_text = requests.post(f"http://Backend:8000/translate", json = payload) # connects to backend/translate url docker.

    for key, text in output_text.json().items():
        st.write(key, ": ", text)

