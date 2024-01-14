from Python_SCPI.devices.powerSupply import powerSupply
from Python_SCPI.SCPI import SCPIInterface

class OWON_ODPXXXX(powerSupply):
    class _owonChannel:
        def __init__(self, interface : SCPIInterface, channelNumber):
            self._IF = interface
            self._CH = channelNumber
            self._cmd_select_channel = "INST:NSEL {channel}"
            self._cmd_set_output = "CHAN:OUTP {state}"
            self._cmd_get_output = "CHAN:OUTP?"
            self._cmd_set_volt = "VOLT {volt}"
            self._cmd_get_volt = "VOLT?"
            self._cmd_set_current = "CURR {curr}"
            self._cmd_get_current = "CURR?"

    def __init__(self, interface : SCPIInterface):
        powerSupply.__init__(self, interface)
        self._channels = [self._owonChannel(interface, 1), self._owonChannel(interface, 2), self._owonChannel(interface, 3)]
        self._cmd_enable_remote = "SYST:REM"
        self._cmd_disable_remote = "SYST:LOC"