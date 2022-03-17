from abc import ABC, abstractmethod

class InvalidOprationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOprationError("Stream is already opened")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOprationError("Stream is already closed")
        self.opened = False
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkSream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from  a memory stream")

stream = MemoryStream()
stream.open()
