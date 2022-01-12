class Directory():
    DIR_MAX_ELEMS = 8

    def __init__(self, name, files=[]):
        self.name = name
        self.files = files.copy()

    def append(self, file):
        if len(self.files) >= self.DIR_MAX_ELEMS:
            print('ERROR: Directory is full.')
            return False

        self.files.append(file)
        return True

    def delete(self, file):
        if file in self.files:
            self.files.remove(file)
        else:
            print('ERROR: No such file is found in current directory.')

    def move(self, file, path):
        if(type(path).__name__ != 'Directory'):
            print('ERROR: Destination is wrong. It\'s not a Directory.')
        elif(path.append(file)):
            self.delete(file)
        else:
            print('ERROR: Some error occured. Move wasn\'t executed.')

    def list_files(self):
        for file in self.files:
            print(file.name, file.ext)

    def list_subdirectories(self, level=0):
        for file in self.files:
            print(level * '--' + f'{file.name}')
            if (type(file).__name__ == 'Directory'):
                file.list_subdirectories(level + 1)
