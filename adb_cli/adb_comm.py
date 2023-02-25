
"""Class Module for Android Command Line Interface"""

import subprocess



class ADBCLITool:
    """Class for ADB command line tools"""

    def __init__(self, command, serial, target_directory=None, receiver_directory=None):
        """Concstructor"""
        self.command = command
        self.serial = serial
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory

    def super_user_mode_android_device(self):
        """Method used to provide privileged access on Android device"""
        return subprocess.run(['adb', '-s', f'{self.serial}', 'root'],
                              capture_output=True, check=False)

    def send_command_to_dut(self):
        """Method used to send arbitrary command to Android device"""
        subprocess.run(['adb', 'shell', f'{self.command}'],
                      check=False)

    def adb_pull_results(self):
        """Method used to pull files from Android device"""
        subprocess.run(['adb', 'pull', f'{self.target_directory}',
                        f'{self.receiver_directory}'], check=False)
