import boto3, os, json
from uuid import uuid4
from datetime import datetime
from ..config.env import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DYNAMODB_TICKET_TABLE

dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

ticket_table = dynamodb.Table(DYNAMODB_TICKET_TABLE)

def create_dynamodb_ticket(user_id, summary_json, file):
    ticket_id = str(uuid4())
    item = {
        "id": ticket_id,
        "user_id": str(user_id),
        "summary_json": json.dumps(summary_json),
        "status": "pending_landlord",
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }
    ticket_table.put_item(Item=item)
    return ticket_id

def scan_tickets():
    response = ticket_table.scan()
    return response.get("Items", [])
