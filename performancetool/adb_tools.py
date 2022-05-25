# Standard Python Imports
from subprocess import Popen, PIPE


class ADBTools:
    '''Standard ADB Tools'''

    def __init(self, adb_command, device_serial):
        self.adb_command = adb_command
        self.device_serial = device_serial


    def root_device(self):
        '''Root Device'''
        proc = Popen(f"adb shell -s {self.device_serial}")
        proc.stdout