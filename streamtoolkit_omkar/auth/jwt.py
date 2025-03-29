import os
import jwt
import requests
from fastapi import Header, HTTPException
from jwt import PyJWKClient
from streamlit import secrets

COGNITO_REGION = secrets.get("AWS_REGION", os.getenv("AWS_REGION"))
USERPOOL_ID = secrets.get("COGNITO_USER_POOL_ID", os.getenv("COGNITO_USER_POOL_ID"))
APP_CLIENT_ID = secrets.get("COGNITO_APP_CLIENT_ID", os.getenv("COGNITO_APP_CLIENT_ID"))
JWKS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{USERPOOL_ID}/.well-known/jwks.json"
jwk_client = PyJWKClient(JWKS_URL)

def get_current_user(Authorization: str = Header(...)):
    token = Authorization.split(" ")[-1]
    try:
        signing_key = jwk_client.get_signing_key_from_jwt(token)
        decoded = jwt.decode(token, signing_key.key, algorithms=["RS256"], audience=APP_CLIENT_ID)
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid JWT: {str(e)}")
