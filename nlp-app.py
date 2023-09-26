import openai
import streamlit as st

# Initialize OpenAI API and server base
#openai.api_key = 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
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"

# Set Streamlit layout
st.set_page_config(layout="wide")

st.title('Web App for Generating Terraform Scripts')
st.caption("🚀 A streamlit app powered by OpenAI LLM")
