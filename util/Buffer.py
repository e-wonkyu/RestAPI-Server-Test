
from util.mutex import Mutex
class Buffer:
    def __init__(self):
        self.count = 0
        self.offset = 0
        self.array = []
    def clear(self):
        del self.array
        self.count = 0
        self.offset = 0
        self.array = []

    def getCount(self):
        return self.count

    def getOffset(self):
        return self.offset

    def setOffset(self,offset):
        self.offset = offset

    def setCount(self,count):
        self.count = count

    def destroy(self):
        del self

