from Python_SCPI.devices.multimeter import multimeter
from Python_SCPI.SCPI import SCPIInterface

class KEITLEY_2015(multimeter):
    def __init__(self, interface : SCPIInterface):
        multimeter.__init__(self, interface)
        self._cmd_take_reading = "READ?"
        self._cmd_set_func = "func '{func}'"
        self._cmd_set_range = "{func}:rang {range:.2f}"

    def setFunction(self, function):
        if(self._cmd_set_func):
            self._IF.write(self._cmd_set_func.format(func = function))

    def setRange(self, function, range:float):
        if(self._cmd_set_range):
            self._IF.write(self._cmd_set_range.format(func = function, range=range))