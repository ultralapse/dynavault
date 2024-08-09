import boto3
import os

TABLE_NAME = os.getenv("TABLE")

# set TABLE_NAME to 'TinypassTable' if it is not set
if TABLE_NAME is None:
    TABLE_NAME = 'TinyPassDevelop-TableTinyPassDevelopC6549CC7-104JGT0OYRKJR'

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
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False
    
def delete_password(user_id, entry_name):
    # Delete password
    dynamodb = get_dynamodb_client()
    response = dynamodb.delete_item (
        TableName=TABLE_NAME,
        Key= {
            'UserID' : {'S' : user_id},
            'EntryName' : {'S' : entry_name}
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(upsert_password('user1', 'entry1', 'password1'))
    print(delete_password('user1', 'entry1'))
