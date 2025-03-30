import streamlit as st
import jwt

def token_input_box():
    return st.text_input("🔐 Paste Cognito ID Token", type="password")

def get_user_from_token_ui(token):
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        st.success(f"✅ Logged in as: {decoded.get('email') or decoded.get('username')}")
        return decoded
    except Exception as e:
        st.error("❌ Invalid token.")
        return None
