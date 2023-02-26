from adb_cli.adb_comm import ADBCLITool


class SendCommand:
    """Class for sending command to Android Device"""

    def __init__(self, command, serial):
        self.command = command
        self.serial = serial
        self.adb_shell = ADBCLITool(serial=self.serial)

    def send_command(self):
        """Method used to send command to android device"""
        self.adb_shell.send_command_to_dut(command=self.command)
