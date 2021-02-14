import os

from utils.s3_client import get_s3_client

from repository.destinations.basic_destination import BasicDestination


class S3Destination(BasicDestination):

    s3_client = None

    def __init__(self):
        super().__init__()
        self.s3_bucket = os.environ.get('OUTPUT_S3_BUCKET')

        # Instantiate and S3 client
        self.s3_client = get_s3_client()

    def save(self, local_path, filename, **_):
        self.s3_client.upload_file(local_path, self.s3_bucket, filename)
