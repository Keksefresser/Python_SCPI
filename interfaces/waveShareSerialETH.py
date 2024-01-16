import socket
import time
from Python_SCPI.SCPI import SCPIInterface

class WaveShareSerialETH(SCPIInterface):
    def __init__(self, IP, PORT, newLineCharacter = "\n", debug = False, timeout = 1000):
        SCPIInterface.__init__(self, newLineCharacter, debug)
        self.IP = IP
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recBuffer = bytearray()
        self.timeout = timeout

    def _open(self):
        self.socket.connect((self.IP, self.PORT))

    def _close(self):
        self.socket.close()

    def _write(self, data : str):
        self.socket.sendall((data+self._newLine).encode("ASCII"))

    def _read(self, size=1) -> str:
        lastTime = time.time()
        while(time.time() - lastTime < self.timeout):
            if(len(self.recBuffer) < size):
                tmp = self.socket.recv(size - len(self.recBuffer))
                lastTime = time.time()
                for b in tmp:
                    self.recBuffer.append(b)
            if(self.recBuffer.count(ord(self._newLine))):
                break
        
        result = bytearray()
        for i in range(size):
            if(len(self.recBuffer) > 0):
                result.append(self.recBuffer.pop(0))
        return result.decode("ASCII", "ignore")