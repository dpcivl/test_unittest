class FileService:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)

    def read_from_file(self):
        with open(self.file_name, 'r') as file:
            return file.read()
