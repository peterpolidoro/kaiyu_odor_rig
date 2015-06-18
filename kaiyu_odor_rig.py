from __future__ import print_function, division
from modular_device import ModularDevices
import time
import yaml


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
        self._debug_print('Initializing KaiyuOdorRig...')
        modular_devices = ModularDevices()

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

    def setup_mfcs(self,mfc_settings_file_path):
        mfc_settings_stream = open(mfc_settings_file_path, 'r')
        mfc_settings = yaml.load(mfc_settings_stream)
        flow_settings = [mfc_settings['mfc_setting_0'],mfc_settings['mfc_setting_1'],0]
        self.psc.set_all_channels_off()
        self._debug_print('set_all_channels_off()')
        self.ami.set_mfc_flows(flow_settings)
        self._debug_print('set_mfc_flows(' + str(flow_settings) + ')')
        self._debug_print('sleeping for ' + str(mfc_settings['sleep_duration']) + 's...')
        time.sleep(mfc_settings['sleep_duration'])

    def run_protocol(self,protocol_file_path):
        protocol_stream = open(protocol_file_path, 'r')
        protocol = yaml.load(protocol_stream)
        for step in protocol:
            self.psc.set_channels_on(step['channels_on'])
            self._debug_print('set_channels_on(' + str(step['channels_on']) + ')')
            self._debug_print('sleeping for ' + str(step['sleep_duration']) + 's...')
            time.sleep(step['sleep_duration'])
            self.psc.set_all_channels_off()
            self._debug_print('set_all_channels_off()')

    def _debug_print(self, *args):
        if self._debug:
            print(*args)


# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    debug = True
    odor_rig = KaiyuOdorRig(debug=debug)
    odor_rig.run()
