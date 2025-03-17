from aws_cdk import (
    Stack,
    Token,
    aws_s3 as s3,
)

class CdkDemoAppStack(Stack):
    def __init__(self, scope, construct_id, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_bucket = s3.Bucket(self, "MyFirstBucket")
        
        # Check if bucket name is a Token
        if Token.is_unresolved(my_bucket.bucket_name):
            print("Bucket name is a Token")
        elif not Token.is_unresolved(my_bucket.bucket_name) and len(my_bucket.bucket_name) <10:
            raise ValueError("Maximum length of bucket name is 10 characters")
