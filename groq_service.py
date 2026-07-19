from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

@st.cache_resource
def get_client():
    return Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )