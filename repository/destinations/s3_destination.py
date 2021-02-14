import os

import boto3

from repository.destinations.basic_destination import BasicDestination


class S3Destination(BasicDestination):

    s3_client = None

    def __init__(self):
        super().__init__()
        self.s3_bucket = os.environ.get('OUTPUT_S3_BUCKET')

        # Instantiate and S3 client
        self.s3_client = boto3.session.Session().client(
            service_name='s3',
            region_name=os.environ.get('S3_REGION'),
            use_ssl=True,
            endpoint_url=os.environ.get('S3_ENDPOINT'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )

    def save(self, local_path, filename, **_):
        self.s3_client.upload_file(local_path, self.s3_bucket, filename)
