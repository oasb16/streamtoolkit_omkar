import streamlit as st

def token_input_box(label="Paste your Cognito ID Token here"):
    return st.text_input(label, type="password")
