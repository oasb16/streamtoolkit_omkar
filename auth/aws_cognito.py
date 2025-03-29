
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def create_user_pool(pool_name):
    client = boto3.client('cognito-idp')
    response = client.create_user_pool(PoolName=pool_name)
    return response["UserPool"]["Id"]

def create_user_pool_client(user_pool_id, client_name):
    client = boto3.client('cognito-idp')
    response = client.create_user_pool_client(
        UserPoolId=user_pool_id,
        ClientName=client_name,
        GenerateSecret=True
    )
    return response["UserPoolClient"]["ClientId"]
