import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

from my_pipeline_project.my_pipeline_app_stage import MyPipelineAppStage


class MyPipelineProjectStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        source = (
            CodePipelineSource.git_hub(
                "nhatnguyen-agilityio/cdk-training",
                "dev",
                authentication=cdk.SecretValue.secrets_manager(
                    "github-token-secret"
                )
            )
        )

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="MyPipeline",
            synth=ShellStep(
                "Synth",
                input=source,
                commands=[
                    "cd my_pipeline_project",
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
                primary_output_directory="my_pipeline_project/cdk.out",
            ),
        )

        stage = pipeline.add_stage(
            MyPipelineAppStage(
                self,
                "MyPipelineAppStageTest",
                env=cdk.Environment(
                    account="194722436838", region="us-east-1"
                ),
            )
        )

        stage.add_post(
            ShellStep(
                "validate",
                input=source,
                commands=[
                    "cd my_pipeline_project",
                    "sh ../tests/validate.sh"
                ],
            )
        )
