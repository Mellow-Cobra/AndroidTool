# Standard Imports
import json
import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QWidget, QPushButton, QMainWindow, QApplication, QGridLayout, \
    QTabWidget, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QRunnable, QThreadPool
from pathlib import Path
# Android Tool Imports
from routines.gfx_bench_routine import GFXBench
from routines.send_command_routine import SendCommand
from constants import TEST_CONFIG, TARG_DIR, RECV_DIR, DUT_SN, GFXBENCH, STANDARD_TEST_CONFIG_PATH

class SendCommandThread(QRunnable):
    """Thread class used to send a command to Android Application"""

    def __init__(self, command, serial):
        """Constructor"""
        super().__init__()
        self.command = command
        self.serial = serial

    def run(self):
        """Method used to run command thread"""
        command_execution_thread = SendCommand(command=self.command,
                                               serial=self.serial)
        command_execution_thread.send_command()


class GFXBenchThread(QRunnable):
    """Thread class used to run benchmark application"""

    def __init__(self, benchmark, serial, test_config, target_directory, receiver_directory):
        """Constructor"""
        super().__init__()
        self.benchmark = benchmark
        self.serial = serial
        self.test_config = test_config
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory

    def run(self):
        gfx_bench_routine = GFXBench(benchmark=self.benchmark, serial=self.serial,
                                     test_config=self.test_config,
                                     target_directory=self.target_directory,
                                     receiver_directory=self.receiver_directory)
        gfx_bench_routine.execute_manhattan_test_case()
class MainWindow(QWidget):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("androidbenchmarktool")
        self.setGeometry(500, 500, 500, 500)

        # Main Layout
        main_layout = QVBoxLayout()

        # Tab Layout
        self.benchmark_tab = QWidget()
        self.config_tab = QWidget()
        self.command_tab = QWidget()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.benchmark_tab, "Benchmarks")
        self.tabs.addTab(self.command_tab, "Send Command")
        self.tabs.addTab(self.config_tab, "Configuration")
        self.test_config = None

        # Benchmark Tab Layout
        self.benchmark_tab.layout = QHBoxLayout()

        # GFX Bench Control Sub Panel Layout
        gfx_bench_layout = QVBoxLayout()
        self.manahattan_311 = QPushButton("Manhattan")
        self.manahattan_311.clicked.connect(self.onclick_manhattan)
        self.benchmark = self.manahattan_311.text()
        self.aztec_ruins_open_gl = QPushButton("Aztec Ruins")
        gfx_bench_layout.addWidget(self.manahattan_311)
        gfx_bench_layout.addWidget(self.aztec_ruins_open_gl)

        # Antutu AI Benchmark
        ai_benchmark_layout = QVBoxLayout()
        self.ai_antutu = QPushButton("Run Antutu AI")
        ai_benchmark_layout.addWidget(self.ai_antutu)

        self.benchmark_tab.setLayout(self.benchmark_tab.layout)
        self.benchmark_tab.layout.addLayout(gfx_bench_layout)
        self.benchmark_tab.layout.addLayout(ai_benchmark_layout)

        # Thread Pool Instantiation
        self.thread_pool = QThreadPool.globalInstance()

        # Send Command Tab Layout
        self.command_tab.layout = QVBoxLayout()

        # Command Tab Widgets
        command_tab_layout = QGridLayout()
        self.command_to_send = QLineEdit()
        self.command_to_send_label = QLabel("Enter Comamnd: ")
        self.send_command_button = QPushButton("Send Command")
        self.send_command_button.clicked.connect(self.on_send_command)
        command_tab_layout.addWidget(self.command_to_send_label, 0, 0)
        command_tab_layout.addWidget(self.command_to_send, 0, 1)
        command_tab_layout.addWidget(self.send_command_button, 1, 1, 1, 1)

        self.command_tab.setLayout(self.command_tab.layout)
        self.command_tab.layout.addLayout(command_tab_layout)

        # Configuration Tab Layout
        self.config_tab.layout = QVBoxLayout()

        # Config Tab Widgets
        config_tab_layout = QGridLayout()
        self.device_serial = QLineEdit()
        self.device_serial_label = QLabel("Enter device serial here: ")
        self.target_directory = QLineEdit()
        self.target_directory_label = QLabel("Enter target directory here: ")
        self.receiving_directory = QLineEdit()
        self.receiving_directory_label = QLabel("Enter receiving directory here: ")
        self.test_config_directory = QLineEdit()
        self.test_config_directory_label = QLabel("Enter Location of Test Config File")
        self.load_config = QPushButton("Load Configuration")
        self.load_config.clicked.connect(self.on_load_test_config)
        self.test_config_directory.setText(STANDARD_TEST_CONFIG_PATH)
        config_tab_layout.addWidget(self.device_serial_label, 0, 0)
        config_tab_layout.addWidget(self.device_serial, 0, 1)
        config_tab_layout.addWidget(self.target_directory_label, 1, 0)
        config_tab_layout.addWidget(self.target_directory, 1, 1)
        config_tab_layout.addWidget(self.receiving_directory_label, 2, 0)
        config_tab_layout.addWidget(self.receiving_directory, 2, 1)
        config_tab_layout.addWidget(self.test_config_directory_label, 3, 0)
        config_tab_layout.addWidget(self.test_config_directory, 3, 1)
        config_tab_layout.addWidget(self.load_config, 4, 1, 1, 1)

        self.config_tab.setLayout(self.config_tab.layout)
        self.config_tab.layout.addLayout(config_tab_layout)

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def onclick_manhattan(self):
        """Event handler for benchmark manhattan"""
        gfx_bench_thread = GFXBenchThread(benchmark=self.benchmark,
                                          serial=self.device_serial.text(),
                                          test_config=self.test_config_directory.text(),
                                          target_directory=self.target_directory.text(),
                                          receiver_directory=self.receiving_directory.text())
        self.thread_pool.start(gfx_bench_thread)

    def on_send_command(self):
        """Event Handler for sending command to Android Device"""
        send_command_thread = SendCommandThread(command=self.command_to_send.text(),
                                                serial=self.device_serial.text())
        self.thread_pool.start(send_command_thread)

    def on_load_test_config(self):
        """Event Handler for loading test configuration from JSON"""
        with open(Path(STANDARD_TEST_CONFIG_PATH), mode='r', encoding='utf-8') as test_config:
            self.test_config = json.load(test_config)
        self.device_serial.setText(self.test_config[TEST_CONFIG][DUT_SN])
        self.receiving_directory.setText(self.test_config[TEST_CONFIG][RECV_DIR])
        self.target_directory.setText(self.test_config[TEST_CONFIG][TARG_DIR])



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
