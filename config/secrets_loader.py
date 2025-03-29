
import os
from dotenv import load_dotenv

def load_secrets():
    load_dotenv()
    return {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "google_client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "google_client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
    }
