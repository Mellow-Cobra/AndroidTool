
"""Class Module for Android Command Line Interface"""

import subprocess



class ADBCLITool:
    """Class for ADB command line tools"""

    def __init__(self, command):
        """Concstructor"""
        self.command = command

    def super_user_mode_android_device(self):
        """Method used to provide privileged access on Android device"""
        return subprocess.run(['adb', 'root'], capture_output=True)
