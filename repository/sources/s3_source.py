import os

from utils.s3_client import get_s3_client

from repository.sources.basic_source import BasicSource


class S3Source(BasicSource):

    s3_client = None

    def __init__(self):
        super().__init__()
        self.s3_bucket = os.environ.get('INPUT_S3_BUCKET')

        # Instantiate and S3 client
        self.s3_client = get_s3_client()

    def list(self, **_):
        elements = {}

        for element in self.s3_client.list_objects_v2(Bucket=self.s3_bucket).get('Contents'):
            element_name = element['Key']
            elements[element_name] = element['LastModified']

        return elements

    def copy(self, filename, destination, **_):
        self.s3_client.download_file(self.s3_bucket, filename, destination)
