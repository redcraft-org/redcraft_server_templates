import os
import json

from repository.sources.basic_source import BasicSource
from repository.sources.s3_source import S3Source

from repository.destinations.basic_destination import BasicDestination
from repository.destinations.s3_destination import S3Destination

class RepositoryManager():

    def __init__(self, source_type=None, destination_type=None):

        if not source_type:
            source_type = os.environ.get('SOURCE')

        if not destination_type:
            destination_type = os.environ.get('DESTINATION')

        if source_type == 's3':
            self.source = S3Source()
        else:
            self.source = BasicSource()

        if destination_type == 's3':
            self.destination = S3Destination()
        else:
            self.destination = BasicDestination()

    def list(self, **kwargs):
        return self.source.list(**kwargs)

    def copy(self, filename, destination, **kwargs):
        return self.source.copy(filename, destination, **kwargs)

    def save(self, downloaded_binary, source, name, url, **kwargs):
        return self.destination.save(downloaded_binary, source, name, url, **kwargs)
