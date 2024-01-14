from SCPI import SCPI, SCPIInterface

class powerSupply(SCPI):
    class _powerSupplyChannel:
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

        def _selectChannel(self):
            if(self._cmd_select_channel):
                channel = self._CH
                self._IF.write(self._cmd_select_channel.format(channel))

        def ON(self):
            if(self._cmd_set_output):
                self._selectChannel()
                channel = self._CH
                state = 1
                self._IF.write(self._cmd_set_output.format(channel, state))

        def OFF(self):
            if(self._cmd_set_output):
                self._selectChannel()
                channel = self._CH
                state = 0
                self._IF.write(self._cmd_set_output.format(channel, state))

        @property
        def volt(self):
            if(self._cmd_get_volt):
                self._selectChannel()
                channel = self._CH
                self._IF.write(self._cmd_get_volt.format(channel))
                return float(self._IF.read(40))
        
        @volt.setter
        def volt(self, value):
            if(self._cmd_set_volt):
                self._selectChannel()
                channel = self._CH
                volt = value
                self._IF.write(self._cmd_set_volt.format(channel, volt))




    def __init__(self, interface : SCPIInterface):
        SCPI.__init__(self, interface)
        self._channels = [self._powerSupplyChannel(interface, 1)]
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