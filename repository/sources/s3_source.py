import os

import boto3

from repository.sources.basic_source import BasicSource


class S3Source(BasicSource):

    s3_client = None

    def __init__(self):
        self.s3_bucket = os.environ.get('INPUT_S3_BUCKET')

        # Instantiate and S3 client
        self.s3_client = boto3.session.Session().client(
            service_name='s3',
            region_name=os.environ.get('S3_REGION'),
            use_ssl=True,
            endpoint_url=os.environ.get('S3_ENDPOINT'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )

    def list(self, **kwargs):
        elements = {}

        for element in self.s3_client.list_objects_v2(Bucket=self.s3_bucket).get('Contents'):
            element_name = element['Key']
            elements[element_name] = element['LastModified']

        return elements

    def copy(self, filename, destination, **kwargs):
        self.s3_client.download_file(self.s3_bucket, filename, destination)
