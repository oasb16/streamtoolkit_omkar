import boto3
import os
import json

def fetch_to_env_file(secret_name="gpt4o-wrapper", region_name="us-east-1", out_file=".env"):
    client = boto3.client("secretsmanager", region_name=region_name)
    secret_value = client.get_secret_value(SecretId=secret_name)
    secrets = json.loads(secret_value['SecretString'])
    with open(out_file, "w") as f:
        for k, v in secrets.items():
            f.write(f"{k}={v}\n")
    print(f"[✓] Secrets written to {out_file}")

if __name__ == "__main__":
    fetch_to_env_file()
