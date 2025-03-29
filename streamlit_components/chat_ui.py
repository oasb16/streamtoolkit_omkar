
import streamlit as st

def gpt_chatbox(session_id):
    st.header("Chat")
    prompt = st.text_input("Ask something:", key=f"{session_id}_input")
    if prompt:
        st.write(f"Processing: {prompt}")
