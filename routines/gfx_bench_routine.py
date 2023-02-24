

from androidbenchmarktool.adb_cli.adb_comm import ADBCLITool

class Manhattan:
    """Class method used to run gfx bench Manhattan 3.1"""

    def __init__(self, benchmark):
        """Constructor"""
        self.benchmark = benchmark

    def execute(self):
        """Method used to run Manhattan Benchmark"""
        adb_shell = ADBCLITool(self.benchmark)