import aws_cdk as core
import aws_cdk.assertions as assertions

from tinypass.tinypass_stack import TinypassStack

# example tests. To run these tests, uncomment this file along with the example
# resource in tinypass/tinypass_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TinypassStack(app, "tinypass")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
