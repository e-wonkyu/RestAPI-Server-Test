from util.Buffer import Buffer
from util.mutex import Mutex

# 파일 입출력 관련 상수
append = 0
readonly = 1
write = 2
create = 3
binary = 4
text = 5
update = 6
writebinary = 7

mode = ['a','r','w','x','b','t','+','wb']
class FileBuffer:
    def __init__(self,path):
        self.buffer = Buffer()
        self.path = path
        self.mutex = Mutex()
        self.fd = None
    def readFile(self,modenum=readonly):
        try:
            self.mutex.lock()
            self.fd = open(self.path,mode=mode[modenum],encoding='UTF-8')
            self.buffer.array = self.fd.read()
            self.fd.close()
            self.mutex.unlock()
            return True
        except Exception as e:
            print("ReadFile Error : ",e)
            self.mutex.unlock()
            return False

    def writeFile(self,writeBuffer,modenum=write):
        try:
            if not writeBuffer:
                return False
            self.mutex.lock()
            self.buffer.array = writeBuffer
            self.fd = open(self.path, mode=mode[modenum], encoding='UTF-8')
            self.buffer.count = self.fd.write(writeBuffer)
            self.fd.close()
            self.mutex.unlock()
            return True
        except Exception as e:
            print("Write File Error : ",e)
            self.mutex.unlock()
    def getBufferlen(self):
        return self.buffer.count

    def destroy(self):
        del self

