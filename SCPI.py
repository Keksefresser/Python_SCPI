class SCPIInterface:
    def __init__(self, newLineCharacter = "\n"):
        self._newLine = newLineCharacter
        pass

    def open(self):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def close(self):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def write(self, data : str):
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

    def read(self, size=1) -> str:
        raise NotImplementedError("Function not implemented. Implementation is expected in derived class.")

class SCPI:
    def __init__(self, interface : SCPIInterface):
        self._IF = interface
        self._cmd_get_id = "*IDN?\n"

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