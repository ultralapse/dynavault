import boto3
import os

TABLE_NAME = os.getenv("TABLE")

def get_dynamodb_client():
    return boto3.client('dynamodb')

# Add an entry with certain attribute
def upsert_password(user_id, entry_name, password):
    dynamodb = get_dynamodb_client()
    response = dynamodb.put_item(
        TableName=TABLE_NAME,
        Item={
            'UserID': {'S': user_id},
            'EntryName': {'S': entry_name},
            'Password': {'S': password}
        }
    )
    print(response)
