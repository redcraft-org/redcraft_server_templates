import os

import boto3


def get_s3_client():
    return boto3.session.Session().client(
        service_name='s3',
        region_name=os.environ.get('S3_REGION'),
        use_ssl=True,
        endpoint_url=os.environ.get('S3_ENDPOINT'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
