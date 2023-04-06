import json

from util.mutex import Mutex


class JsonConfigParser:
    def __init__(self,path):
        self.path = path
        self.jsondata = None
        self.mutex = Mutex()

    def readJsonConfig(self):
        try:
            self.mutex.lock()
            with open(self.path, 'r') as f:
                self.jsondata = json.load(f)
                return True
            self.mutex.unlock()
        except Exception as e:
            print("Json Config Parser Error : ",e)
            self.mutex.unlock()
            return False
