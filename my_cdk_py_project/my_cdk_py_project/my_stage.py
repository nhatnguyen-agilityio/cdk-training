from aws_cdk import Stage
from constructs import Construct
from .app_stack import AppStack
from .database_stack import DatabaseStack

# Define the stage
class MyStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stage goes here
        AppStack(self, "AppStack")
        DatabaseStack(self, "DatabaseStack")
