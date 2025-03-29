import os
import streamlit as st

def get_env_var(key, default=None):
    return st.secrets.get(key, os.getenv(key, default))

BACKEND_URL = get_env_var("BACKEND_URL")
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")
AWS_REGION = get_env_var("AWS_REGION")
DYNAMODB_TICKET_TABLE = get_env_var("DYNAMODB_TICKET_TABLE")
AWS_ACCESS_KEY_ID = get_env_var("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_var("AWS_SECRET_ACCESS_KEY")
COGNITO_USER_POOL_ID = get_env_var("COGNITO_USER_POOL_ID")
COGNITO_APP_CLIENT_ID = get_env_var("COGNITO_APP_CLIENT_ID")
