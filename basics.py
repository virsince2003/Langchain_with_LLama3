import streamlit as st
from langchain_community.llms import Ollama
ollama = Ollama(
    model="llama3"
)
    # base_url='http://localhost:11434'


st.title("Langchain basics")
input = st.text_input("Enter your text here")
if input:
    st.write(ollama.invoke(input))