import boto3
import db
import json


def handler(event, context):
    api_path = event.get('path', '')

    # Get JSON body of HTTP request
    body = json.loads(event.get('body', '{}'))

    # Get user_id, entry_name, and password from JSON body
    UserID = body.get('UserID', '')
    EntryName = body.get('EntryName', '')
    Password = body.get('Password', '')

    # What request is it (GET, POST, PUT, DELETE)?
    method = event.get('httpMethod', '')

    match method:
        case 'POST':
            # Insert password for user1, entry1, password1 through JSON body of HTTP request
            result = db.upsert_password(UserID, EntryName, Password)
            if result:
                return {
                    'statusCode': 200,
                    'body': 'Password inserted\n'
                }
            return {
                'statusCode': 400,
                'body': 'Error: The Password was not successfully inserted\n'
            }

    # match api_path:
    #     case '/':
    #         return {
    #             'statusCode': 200,
    #             'body': 'Hello from Tinypass!'
    #         }
    #     case '/health':
    #         return {
    #             'statusCode': 200,
    #             'body': 'OK'
    #         }
    #     case _:
    #         return {
    #             'statusCode': 404,
    #             'body': 'Not Found'
    #         }