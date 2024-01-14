import socket
from Python_SCPI.SCPI import SCPIInterface

class WaveShareSerialETH(SCPIInterface):
    def __init__(self, IP, PORT, newLineCharacter = "\n"):
        SCPIInterface.__init__(self, newLineCharacter)
        self.IP = IP
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recBuffer = bytearray()

    def open(self):
        self.socket.connect((self.IP, self.PORT))

    def close(self):
        self.socket.close()

    def write(self, data : str):
        self.socket.sendall((data+self._newLine).encode("ASCII"))

    def read(self, size=1) -> str:
        if(len(self.recBuffer) < size):
            tmp = self.socket.recv(size - len(self.recBuffer))
            for b in tmp:
                self.recBuffer.append(b)
        
        result = bytearray()
        for i in range(size):
            if(len(self.recBuffer) > 0):
                result.append(self.recBuffer.pop(0))
        return result.decode("ASCII", "ignore")