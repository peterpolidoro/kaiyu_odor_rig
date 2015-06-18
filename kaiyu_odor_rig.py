from __future__ import print_function, division
from modular_device import ModularDevices
import time

DEBUG = True
BAUDRATE = 9600

class KaiyuOdorRig(object):
    '''
    '''

    def __init__(self,*args,**kwargs):
        if 'debug' in kwargs:
            self._debug = kwargs['debug']
        else:
            kwargs.update({'debug': DEBUG})
            self._debug = DEBUG
        modular_devices = ModularDevices(try_ports=ports)

        modular_device_name = 'power_switch_controller'
        try:
            dev_dict = modular_devices[modular_device_name]
        except KeyError:
            raise HybridizerError('Could not find ' + modular_device_name + '. Check connections and permissions.')
        if len(dev_dict) > 1:
            raise HybridizerError('More than one ' + modular_device_name + ' found. Only one should be connected.')
        self.psc = dev_dict[dev_dict.keys()[0]]
        self._debug_print('Found ' + modular_device_name + ' on port ' + str(self.psc.get_port()))

        modular_device_name = 'aalborg_mfc_interface'
        try:
            dev_dict = modular_devices[modular_device_name]
        except KeyError:
            raise HybridizerError('Could not find ' + modular_device_name + '. Check connections and permissions.')
        if len(dev_dict) > 1:
            raise HybridizerError('More than one ' + modular_device_name + ' found. Only one should be connected.')
        self.ami = dev_dict[dev_dict.keys()[0]]
        self._debug_print('Found ' + modular_device_name + ' on port ' + str(self.ami.get_port()))

    def run(self):
        self.psc.set_all_channels_off()
        self.ami.set_mfc_flows([10,10,10])
        time.sleep(10)
        self.psc.set_channels_on([1,3,5])
        time.sleep(5)
        self.psc.set_all_channels_off()

    def _debug_print(self, *args):
        if self._debug:
            print(*args)


# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    debug = True
    odor_rig = KaiyuOdorRig(debug=debug)
    odor_rig.run()
