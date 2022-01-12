class Log():
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def read(self):
        return self.contents

    def append(self, line):
        self.contents += line
