# to import the module for abstract creation
from abc import ABC, abstractmethod

# How to create custom error that doesn't exit in python


class InvalidOperationError(Exception):
    pass

# base class(where multiple methods are defined) should not be instantiable, we must make the class ABSTRACT and make only their subclasses instantiable


class Stream(ABC):     # Make the stream inherit the class ABC
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

    @abstractmethod  # define an abstract to be used by other class
    def read(self):
        pass

#  Creating an Inheritance


class FileStream(Stream):
    def read(self):
        print("reading file")


class NetworkStream(Stream):
    def read(self):
        print("reading file network files.")


m = NetworkStream
