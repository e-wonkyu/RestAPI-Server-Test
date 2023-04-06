from threading import Lock

class Mutex:
    def __init__(self):
        self.mutex = Lock()
    def lock(self):
        self.mutex.acquire()
    def unlock(self):
        self.mutex.release()
    def destroy(self):
        del self