
import streamlit as st
from streamlit_oauth import OAuth2Login

def use_google_login(client_id, client_secret, redirect_uri):
    return OAuth2Login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        provider="google"
    ).login()
