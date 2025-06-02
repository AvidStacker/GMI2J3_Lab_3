
class FileService:
    def read_file(self, filepath):
        with open(filepath, 'r') as f:
            return f.read()
