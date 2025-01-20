

# How to create custom error that doesn't exit in python
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File already close")
        self.opened = False

#  Creating an Inheritance


class FileStream(Stream):
    def read(self):
        print("reading file")


class NetworkStream(Stream):
    def read(self):
        print("reading file network files.")
