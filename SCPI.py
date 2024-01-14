class SCPIInterface(object):
    def __init__(self, newLineCharacter = "\n", debug : bool = False):
        self._newLine = newLineCharacter
        self._dbg = debug
        pass

    def open(self):
        self._open()

    def close(self):
        self._close()

    def write(self, data : str):
        if(self._dbg):
            print(f"[TX]: {data}")
        self._write(data)

    def read(self, size=1) -> str:
        data = self._read(size)
        if(self._dbg):
            print(f"[RX]: {data}")
        return data

    def _open(self):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def _close(self):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def _write(self, data : str):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def _read(self, size=1) -> str:
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

class SCPI(object):
    def __init__(self, interface : SCPIInterface):
        self._IF = interface
        self._cmd_get_id = "*IDN?"

    def connect(self) -> bool:
        try:
            self._IF.open()
            self.getID()
            return True
        except:
            return False

    def disconnect(self):
        self._IF.close()

    def getID(self) -> str:
        self._IF.write(self._cmd_get_id)
        return self._IF.read(40)