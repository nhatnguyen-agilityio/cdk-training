#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_pipeline_project.my_pipeline_project_stack import MyPipelineProjectStack


app = cdk.App()
MyPipelineProjectStack(app, "MyPipelineProjectStack",
    env=cdk.Environment(account="194722436838", region="us-east-1")
    )

app.synth()
