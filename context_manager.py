
class Open_File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Testing the file!')

#Check if the file is already closed or not
print(f.closed)

