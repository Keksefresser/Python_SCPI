from Python_SCPI.SCPI import SCPI, SCPIInterface

class multimeter(SCPI):
    def __init__(self, interface : SCPIInterface):
        SCPI.__init__(self, interface)
        self._cmd_enable_remote = "SYST:REM"
        self._cmd_disable_remote = "SYST:LOC"
        self._cmd_reset = "*RST"
        self._cmd_take_reading = ""

    def remote(self):
        if(self._cmd_enable_remote):
            self._IF.write(self._cmd_enable_remote)

    def local(self):
        if(self._cmd_disable_remote):
            self._IF.write(self._cmd_disable_remote)
        
    def takeReading(self) -> float:
        if(self._cmd_take_reading):
            self._IF.write(self._cmd_take_reading)
            return float(self._IF.read(40))
        
    def reset(self):
        if(self._cmd_reset):
            self._IF.write(self._cmd_reset)
        