import openai
import streamlit as st
from streamlit_pills import pills
import os
from dotenv import load_dotenv

load_dotenv() # Load environment
openai.api_key = os.getenv("openAI") # Get API key from environment variable
# set the title 
st.title("Python Script Generator")
# add the subheader
st.subheader("Streamlit + OpenAI")
# An entry field for user input
user_input = st.text_input("", placeholder="Enter the title here...", key="input")
if st.button("Submit", type="primary"):
    result_box = st.empty()
    report = []
    # Loop over the resonse
    for text in openai.Completion.create(model="text-davinci-003",
                                        prompt = user_input,
                                        max_tokens = 1000,
                                        temperature = 0.5,
                                        stream = True):
        # Append new resonses and then strip out any empty strings
        report.append(text.choices[0].text)
        result = "".join(report).strip()
        
        # Display results in python scripting format
        result_box.markdown(f'````python{result}')