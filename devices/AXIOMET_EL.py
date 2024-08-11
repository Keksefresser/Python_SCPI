from Python_SCPI.devices.electronicLoad import electronicLoad
from Python_SCPI.SCPI import SCPIInterface

class AXIOMET_EL(electronicLoad):
    def __init__(self, interface : SCPIInterface):
        electronicLoad.__init__(self, interface)
        self._cmd_set_curr = "CURR {val:.3f}"
