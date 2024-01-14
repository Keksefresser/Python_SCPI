from Python_SCPI.SCPI import SCPI, SCPIInterface

class powerSupplyChannel(object):
    def __init__(self, interface : SCPIInterface, channelNumber):
        self._IF = interface
        self._CH = channelNumber
        self._cmd_select_channel = ""
        self._cmd_set_output = ""
        self._cmd_get_output = ""
        self._cmd_set_volt = ""
        self._cmd_get_volt = ""
        self._cmd_set_current = ""
        self._cmd_get_current = ""
        self._cmd_meas_volt = ""
        self._cmd_meas_current = ""
        self._cmd_meas_power = ""

    def _selectChannel(self):
        if(self._cmd_select_channel):
            self._IF.write(self._cmd_select_channel.format(channel = self._CH))

    @property
    def state(self):
        if(self._cmd_get_output):
            self._selectChannel()
            self._IF.write(self._cmd_get_output.format(channel = self._CH))
            return int(self._IF.read(40))
    
    @state.setter
    def state(self, value):
        if(self._cmd_set_output):
            self._selectChannel()
            self._IF.write(self._cmd_set_output.format(channel = self._CH, state = value))
            self.state

    def ON(self):
        self.state = 1

    def OFF(self):
        self.state = 0

    @property
    def voltage(self):
        if(self._cmd_get_volt):
            self._selectChannel()
            self._IF.write(self._cmd_get_volt.format(channel = self._CH))
            return float(self._IF.read(40))
    
    @voltage.setter
    def voltage(self, value):
        if(self._cmd_set_volt):
            self._selectChannel()
            self._IF.write(self._cmd_set_volt.format(channel = self._CH, volt = value))
            self.voltage

    @property
    def current(self):
        if(self._cmd_get_current):
            self._selectChannel()
            self._IF.write(self._cmd_get_current.format(channel = self._CH))
            return float(self._IF.read(40))
    
    @current.setter
    def current(self, value):
        if(self._cmd_set_current):
            self._selectChannel()
            self._IF.write(self._cmd_set_current.format(channel = self._CH, curr = value))
            self.current

    def measureVoltage(self) -> float:
        if(self._cmd_meas_volt):
            self._selectChannel()
            self._IF.write(self._cmd_meas_volt.format(channel = self._CH))
            return float(self._IF.read(40))
        
    def measureCurrent(self) -> float:
        if(self._cmd_meas_current):
            self._selectChannel()
            self._IF.write(self._cmd_meas_current.format(channel = self._CH))
            return float(self._IF.read(40))
        
    def measurePower(self) -> float:
        if(self._cmd_meas_power):
            self._selectChannel()
            self._IF.write(self._cmd_meas_power.format(channel = self._CH))
            return float(self._IF.read(40))





class powerSupply(SCPI):
    def __init__(self, interface : SCPIInterface):
        SCPI.__init__(self, interface)
        self._channels = [powerSupplyChannel(interface, 1)]
        self._cmd_enable_remote = ""
        self._cmd_disable_remote = ""
        self._cmd_select_channel = ""
        self._cmd_enable_channel = ""
        self._cmd_disable_channel = ""

    def remote(self):
        if(self._cmd_enable_remote):
            self._IF.write(self._cmd_enable_remote)

    def local(self):
        if(self._cmd_disable_remote):
            self._IF.write(self._cmd_disable_remote)
        
    def __getitem__(self, key):
        if(key < len(self._channels)):
            return self._channels[key]
        else:
            raise IndexError(f"Index {key} out of range. Num Channels is: {len(self._channels)}")
        
    def __setitem__(self, item, value):
        raise Exception("Overriding channels is not supported.")