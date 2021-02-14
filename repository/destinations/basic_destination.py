import os
from shutil import copyfile


class BasicDestination():

    output_folder = None

    def __init__(self):
        self.output_folder = os.environ.get('OUTPUT_FOLDER', 'plugins')

    def save(self, local_path, filename, **_):
        file_path = os.path.join(self.output_folder, filename)

        copyfile(local_path, file_path)
