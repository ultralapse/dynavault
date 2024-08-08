import boto3


def handler(event, context):
    api_path = event.get('path', '')

    match api_path:
        case '/':
            return {
                'statusCode': 200,
                'body': 'Hello from Tinypass!'
            }
        case '/health':
            return {
                'statusCode': 200,
                'body': 'OK'
            }
        case _:
            return {
                'statusCode': 404,
                'body': 'Not Found'
            }