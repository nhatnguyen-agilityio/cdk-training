from typing import List
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
import aws_cdk.aws_sns as sns
import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_sns_subscriptions as sns_subscriptions
from constructs import Construct

class StateMachineStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        topics: List[sns.Topic],
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        state_machine = sfn.StateMachine(
            self, "StateMachine",
            definition=sfn.Pass(
                self, "StartState",
            ),
        )
        
        func = lambda_.Function(
            self, "LambdaFunction",
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="handler",
            code=lambda_.Code.from_asset("./start-state-machine"),
            environment={
                "STATE_MACHINE_ARN": state_machine.state_machine_arn
            },
        )
        state_machine.grant_start_execution(func)
        
        subscription = sns_subscriptions.LambdaSubscription(func)
        for topic in topics:
            topic.add_subscription(subscription)
