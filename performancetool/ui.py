import sys

# Standard Python Imports
from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QWidget, QAction, \
    QTabWidget, QMainWindow, \
    QStatusBar, QLineEdit, \
    QFormLayout, QVBoxLayout, \
    QHBoxLayout, QRadioButton

# Electromagnetic Ventures LLC Imports

# Global Variables
RESULTS_DIR = "results_dir"
LOG_DIR = "log_out"


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Android Performance Tool")
        self.setGeometry(0, 0, 300, 300)
        self.layout = QVBoxLayout(self)

        # Tabs
        self.tabs = QTabWidget()
        self.benchmark_selection_tab = QWidget()
        self.device_configuration_tab = QWidget()
        self.tools_tab = QWidget()
        self.tabs.resize(300, 200)

        # Add Tabs
        self.tabs.addTab(self.benchmark_selection_tab, "Select Benchmark")
        self.tabs.addTab(self.device_configuration_tab, "Configuration")
        self.tabs.addTab(self.tools_tab, "Tools")

        # Set up Test Benchmark Selection Tab
        self.benchmark_selection_tab.layout = QFormLayout(self)
        self.benchmark_selection_tab.layout.addWidget(QRadioButton("GFX Bench"))
        self.benchmark_selection_tab.setLayout(self.benchmark_selection_tab.layout)

        # Set up Device Tab
        self.device_configuration_tab.layout = QVBoxLayout(self)
        self.serial_input_label = QLabel("Enter DUT Serial Number")
        self.adb_command_input_label = QLabel("Enter ADB Command")
        self.adb_command = QLineEdit()
        self.dut_serial = QLineEdit()
        self.device_configuration_tab.layout.addWidget(self.serial_input_label)
        self.device_configuration_tab.layout.addWidget(self.dut_serial)
        self.device_configuration_tab.layout.addWidget(self.adb_command_input_label)
        self.device_configuration_tab.layout.addWidget(self.adb_command)
        self.device_serial = self.dut_serial.text()
        self.command = self.adb_command.text()
        self.device_configuration_tab.setLayout(self.device_configuration_tab.layout)

        # Set up ADB Tools Tab
        self.tools_tab.layout = QVBoxLayout(self)
        self.root_button = QPushButton("Root DUT")
        self.tools_tab.layout.addWidget(self.root_button)
        self.tools_tab.setLayout(self.tools_tab.layout)


        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.show()

    def get_configuration(self):
        """Load dict of ui elements"""
        configuration = {RESULTS_DIR: self.reuslts_dir.text(),
                         LOG_DIR: self.log_out_dir.text(),
                         }

    def on_click(self):
        Worker(self.command, self.serial)


class Worker():

    def __init__(self, adb_command, device_serial):
        self.adb_command = adb_command


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
