#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_cdk.hello_cdk_stack import HelloCdkStack
from hello_cdk.s3_example_stack import S3ExampleStack


app = cdk.App()
HelloCdkStack(app, "HelloCdkStack", env=cdk.Environment(account="194722436838", region="us-east-1"))
S3ExampleStack(app, "S3ExampleStack", env=cdk.Environment(account="194722436838", region="us-east-1"))

app.synth()
