from Python_SCPI.SCPI import SCPI, SCPIInterface

class electronicLoad(SCPI):
    def __init__(self, interface : SCPIInterface):
        SCPI.__init__(self, interface)
        self._cmd_input_on = "INPUT On"
        self._cmd_input_off = "INPUT Off"
        self._cmd_set_mode = "MODE {mode}"
        self._cmd_set_curr = "CURR {val}"
        self._cmd_reset = "*RST"
        self._cmd_take_reading = ""

    def on(self):
        if(self._cmd_input_on):
            self._IF.write(self._cmd_input_on)

    def off(self):
        if(self._cmd_input_off):
            self._IF.write(self._cmd_input_off)

    def setMode(self, mode):
        if(self._cmd_set_mode):
            self._IF.write(self._cmd_set_mode.format(mode = mode))

    def reset(self):
        if(self._cmd_reset):
            self._IF.write(self._cmd_reset)

    def setCurrent(self, curr:float):
        if(self._cmd_set_mode):
            self._IF.write(self._cmd_set_curr.format(val = curr))