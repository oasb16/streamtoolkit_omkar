import os
import json
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import streamlit as st

SECRET_NAME = os.getenv("AWS_SECRET_NAME", "gpt4o-wrapper")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

def fetch_secrets_from_aws():
    try:
        client = boto3.client("secretsmanager", region_name=AWS_REGION)
        response = client.get_secret_value(SecretId=SECRET_NAME)
        return json.loads(response['SecretString'])
    except (NoCredentialsError, ClientError) as e:
        return {}

def get_env(key, default=None):
    return (
        os.getenv(key)
        or st.secrets.get(key, None)
        or fetch_secrets_from_aws().get(key)
        or default
    )

OPENAI_API_KEY           = get_env("OPENAI_API_KEY")
AWS_REGION               = get_env("AWS_REGION")
AWS_ACCESS_KEY_ID        = get_env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY    = get_env("AWS_SECRET_ACCESS_KEY")
S3_BUCKET                = get_env("S3_BUCKET")
COGNITO_USER_POOL_ID     = get_env("COGNITO_USER_POOL_ID")
COGNITO_APP_CLIENT_ID    = get_env("COGNITO_APP_CLIENT_ID")
DYNAMODB_TABLE           = get_env("DYNAMODB_TABLE")
