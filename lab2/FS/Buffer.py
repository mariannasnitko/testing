class Buffer():
    MAX_BUF_FILE_SIZE = 8

    def __init__(self, name, files):
        self.name = name
        self.queue = files.copy()

    def push(self, elem):
        if len(self.queue) >= self.MAX_BUF_FILE_SIZE:
            print("ERROR: Limit size is reached.")
            return False
        else:
            self.queue.append(elem)
        return True

    def consume(self):
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        else:
            print("Warning: Buffer is empty")
            return False
