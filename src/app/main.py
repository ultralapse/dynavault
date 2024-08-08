import boto3
import db


def handler(event, context):
    api_path = event.get('path', '')

    # Get JSON body of HTTP request
    body = event.get('body', '{}')

    # Get user_id, entry_name, and password from JSON body
    user_id = body.get('user_id', '')
    entry_name = body.get('entry_name', '')
    password = body.get('password', '')

    # What request is it (GET, POST, PUT, DELETE)?
    method = event.get('httpMethod', '')

    match method:
        case 'GET':
            # Insert password for user1, entry1, password1 through JSON body of HTTP request
            

            db.upsert_password('user1', 'entry1', 'password1')

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