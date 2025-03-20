import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class MyPipelineProjectStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="MyPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "nhatnguyen-agilityio/cdk-training",
                    "dev",
                    authentication=cdk.SecretValue.secrets_manager(
                        "github-token-secret"
                    ),
                ),
                commands=[
                    "cd my_pipeline_project",
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        ),
    # Define the artifact for the output
    output=cdk.aws_codepipeline.Artifact("MyArtifact"),
    # Explicitly set the directory to be uploaded
    post_build=ShellStep(
        "PostBuild",
        commands=["echo 'Upload artifacts from cdk.out'"],
        primary_output_directory="cdk.out",  # Explicitly set cdk.out as output
    ),
