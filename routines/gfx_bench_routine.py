

from androidbenchmarktool.adb_cli.adb_comm import ADBCLITool

class GFXBench:
    """Class method used to run gfx bench Manhattan 3.1"""

    def __init__(self, benchmark, command, serial, target_directory, receiver_directory):
        """Constructor"""
        self.benchmark = benchmark
        self.command = command
        self.serial = serial
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory

    def execute(self):
        """Method used to run Manhattan Benchmark"""
        adb_shell = ADBCLITool(self.benchmark)
        d