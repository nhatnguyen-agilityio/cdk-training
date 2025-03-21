import aws_cdk as core
import aws_cdk.assertions as assertions

from state_machine.state_machine_stack import StateMachineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in state_machine/state_machine_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StateMachineStack(app, "state-machine")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
