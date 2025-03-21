from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from aws_cdk import aws_s3_assets as assets
from constructs import Construct


class S3ExampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "MyBucket",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
        )
        
        # Upload a file to S3 during deployment
        asset = assets.Asset(self, "Asset", path="hello_cdk/testing_upload_file.txt")
        
        # Grant read access to the bucket
        bucket.add_to_resource_policy(
            cdk.aws_iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"{bucket.bucket_arn}/*"],
                principals=[cdk.aws_iam.ArnPrincipal("*")],
            )
        )
        
        # Output the bucket name
        # cdk.CfnOutput is used to export values from your AWS CDK stack so you can easily reference them after deployment.
        cdk.CfnOutput(self, "BucketName", value=bucket.bucket_name)
        cdk.CfnOutput(self, "FileS3URL", value=bucket.s3_url_for_object("local-file.txt"))
        