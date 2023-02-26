
"""Class Module for Android Command Line Interface"""

import subprocess



class ADBCLITool:
    """Class for ADB command line tools"""

    def __init__(self, serial):
        """Concstructor"""
        self.serial = serial

    def super_user_mode_android_device(self):
        """Method used to provide privileged access on Android device"""
        return subprocess.run(['adb', '-s', f'{self.serial}', 'root'],
                              capture_output=True, check=False)

    def execute_command_on_dut(self, command):
        """Method used to send arbitrary command to Android device"""
        subprocess.run(['adb', '-s', f'{self.serial}', 'shell', f'{command}'],
                      check=False)

    def run_adb_terminal_command(self, command):
        """Method used run ADB command in terminal"""
        subprocess.run(['adb', '-s', f'{self.serial}', f'{command}'],
                       check=False)

    def adb_pull_results(self, target_directory, receiver_directory):
        """Method used to pull files from Android device"""
        subprocess.run(['adb', '-s', f'{self.serial}', 'pull', f'{target_directory}',
                        f'{receiver_directory}'], check=False)
