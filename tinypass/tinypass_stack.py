from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway
)
from constructs import Construct

class TinypassStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table with partition key UserID and range key EntryName
        table = dynamodb.Table(self, f"Table{construct_id}",
            partition_key=dynamodb.Attribute(name="UserID", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="EntryName", type=dynamodb.AttributeType.STRING)
        )

        dockerFunc = _lambda.DockerImageFunction(
            scope=self,
            id=f"ID{construct_id}",
            function_name=construct_id,
            environment= {
                "TABLE": table.table_name
            },            
            code=_lambda.DockerImageCode.from_image_asset(
                directory="src"
            ),
            timeout=Duration.seconds(900)
        )

        api = apigateway.LambdaRestApi(self, f"API{construct_id}",
            handler=dockerFunc,
            proxy=True,
        )

        table.grant_read_write_data(dockerFunc.role)



        
