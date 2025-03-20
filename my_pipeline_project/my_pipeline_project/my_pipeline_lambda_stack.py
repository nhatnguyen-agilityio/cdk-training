import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, InlineCode, Runtime

class MyLambdaStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        Function(
            self,
            "LambdaFunction",
            runtime=Runtime.NODEJS_18_X,
            handler="index.handler",
            timeout=cdk.Duration.seconds(10),
            code=InlineCode("exports.handler = _ => 'Hello, CDK';"),
        )
