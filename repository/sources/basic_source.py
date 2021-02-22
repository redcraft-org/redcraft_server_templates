import os
from shutil import copyfile


class BasicSource():

    input_folder = None

    def __init__(self):
        self.input_folder = os.environ.get('input_folder', 'plugins')

    def list(self, **_):
        elements = {}

        for element in os.listdir(self.input_folder):
            modified_at = os.path.getmtime(
                os.path.join(self.input_folder, element))
            elements[element] = modified_at

        return elements

    def copy(self, filename, destination, **_):
        file_path = os.path.join(self.input_folder, filename)

        copyfile(file_path, destination)
