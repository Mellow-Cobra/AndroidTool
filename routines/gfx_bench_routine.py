

from adb_cli.adb_comm import ADBCLITool

class GFXBench:
    """Class method used to run gfx bench Manhattan 3.1"""

    def __init__(self, benchmark, serial, test_config, target_directory, receiver_directory):
        """Constructor"""
        self.benchmark = benchmark
        self.serial = serial
        self.test_config = test_config
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory

    def execute(self):
        """Method used to run Manhattan Benchmark"""
        if self.benchmark ==  "Manhattan":
            self.run_manhattan()

    def run_manhattan(self):
        """Method used to iterate through manhattan benchmark from config"""


