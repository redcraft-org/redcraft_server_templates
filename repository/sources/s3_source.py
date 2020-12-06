import os
import re

import boto3

from repository.sources.basic_source import BasicSource


class S3Source(BasicSource):

    s3_client = None

    def __init__(self):
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

    def list(self, **kwargs):
        return self.s3_client.list_objects_v2(Bucket=self.s3_bucket)

    def read(self, filename, **kwargs):
        return self.s3_client.get_object(Bucket=self.s3_bucket)['Body'].read()

    def get_filter_regex(self, filter):
        return re.compile(filter.replace('*', '.+'))
