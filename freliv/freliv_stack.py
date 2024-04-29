from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_function,
    aws_dynamodb as ddb,
    aws_s3 as s3
)
from constructs import Construct

class FrelivStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
            self, "FrelivQueue",
            visibility_timeout=Duration.seconds(300)
        )

        function = lambda_function.Function(self, "DemoCDKFunction",
                                            function_name="cdk_github_demo",
                                            runtime=lambda_function.Runtime.PYTHON_3_12,
                                            code=lambda_function.Code.from_asset('./lambda_code_demo'),
                                            handler="demo_lambda.lambda_handler")
        
        function = lambda_function.Function(self, "DummyLambda",
                                            function_name="cdk_Lambda_code",
                                            runtime=lambda_function.Runtime.PYTHON_3_9,
                                            code=lambda_function.Code.from_asset('./lambda_code_demo'),
                                            handler="lambda_code.lambda_handler")
        
        table = ddb.Table(
            self, 'MyDataTable',
            partition_key=ddb.Attribute(name='id', type=ddb.AttributeType.STRING)
        )

        bucket = s3.Bucket(
            self, "MyUniqueBucket",
            bucket_name="my-unique-bucket-name-Freliv",  # Bucket names must be globally unique
            versioned=True,  # Enable versioning
            encryption=s3.BucketEncryption.S3_MANAGED
        )

