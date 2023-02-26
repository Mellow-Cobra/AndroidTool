import json
import time

from adb_cli.adb_comm import ADBCLITool
from constants import GFXBENCH, MANHATTAN, DISCONNECT


class GFXBench:
    """Class method used to run gfx bench Manhattan 3.1"""

    def __init__(self, benchmark, serial, test_config, target_directory, receiver_directory):
        """Constructor"""
        self.benchmark = benchmark
        self.serial = serial
        self.test_config = test_config
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory
        self.adb_shell = None

    def execute_manhattan_test_case(self):
        """Method used to run Manhattan Benchmark"""
        self.load_test_config()
        self.run_manhattan()
        self.pull_results()

    def run_manhattan(self):
        """Method used to instantiate Android Debug Bridge Comm Manager"""
        for test_case in self.test_config[GFXBENCH][MANHATTAN]:
            command = f'am  broadcast  -a net.kishonti.testfw.ACTION_RUN_TESTS -n ' \
                      f'net.kishonti.gfxbench.vulkan.v50000.corporate/' \
                      f'net.kishonti.benchui.corporate.CommandLineSession -e test_ids "{test_case}" '
            self.adb_shell = ADBCLITool(serial=self.serial)
            self.adb_shell.send_command_to_dut(command=command)
        self.adb_shell.send_command_to_dut(DISCONNECT)


    def pull_results(self):
        """Method to pull results from Android Device after running a test"""
        self.adb_shell = ADBCLITool(serial=self.serial)
        self.adb_shell.adb_pull_results(target_directory=self.target_directory,
                                        receiver_directory=self.receiver_directory)
        self.adb_shell.send_command_to_dut(DISCONNECT)

    def load_test_config(self):
        """Method used to load test config file"""
        with open(self.test_config, mode='r', encoding='utf-8') as test_config:
            self.test_config = json.load(test_config)
            test_config.close()