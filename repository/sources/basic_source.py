import os


class BasicSource():

    input_folder = None

    def __init__(self):
        self.input_folder = os.environ.get('input_folder', 'plugins')

    def list(self, **kwargs):
        return os.listdir(self.input_folder)

    def read(self, filename, **kwargs):
        file_path = os.path.join(self.input_folder, filename)

        # Read file from disk
        with open(file_path, 'rb') as file:
            return file.read()
