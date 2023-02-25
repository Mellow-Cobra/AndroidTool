
# Standard Imports
import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QWidget, QPushButton, QMainWindow, QApplication, QGridLayout, \
    QTabWidget, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QRunnable, QThreadPool

# Android Tool Imports
from routines.gfx_bench_routine import GFXBench

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
        self.tabs = QTabWidget()
        self.tabs.addTab(self.benchmark_tab, "Benchmarks")
        self.tabs.addTab(self.config_tab, "Configuration")

        # Benchmark Tab Layout
        self.benchmark_tab.layout = QHBoxLayout()

        # GFX Bench Control Sub Panel Layout
        gfx_bench_layout = QVBoxLayout()
        self.manahattan_311 = QPushButton("gl_manhattan311_wqhd_off")
        self.manahattan_311.clicked.connect(self.onclick_manhattan_311)
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

        # Configuration Tab Layout
        self.config_tab.layout = QVBoxLayout()

        # Config Tab Widgets
        config_tab_layout = QGridLayout()
        self.device_serial = QLineEdit()
        self.device_serial_label = QLabel("Enter device serial here: ")
        self.target_directory = QLineEdit()
        self.target_directory_label = QLabel("Enter target directory here: ")
        self.receiving_directory = QFileDialog()
        config_tab_layout.addWidget(self.device_serial_label, 0, 0)
        config_tab_layout.addWidget(self.device_serial, 0, 1)
        config_tab_layout.addWidget(self.target_directory_label, 1, 0)
        config_tab_layout.addWidget(self.target_directory, 1, 1)
        config_tab_layout.addWidget(self.receiving_directory, 2, 0)

        self.config_tab.setLayout(self.config_tab.layout)
        self.config_tab.layout.addLayout(config_tab_layout)

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)





    def onclick_manhattan_311(self):
        """Event handler for benchmark manhattan"""
        GFXBench(benchmark=self.benchmark,
                 serial=self.device_serial.text(),
                 command=self.command.text(),
                 target_directory=self.target_directory.text(),
                 receiver_directory=self.receiving_directory.text())


class GFXBench(QRunnable):
    """Thread class used to run benchmark application"""

    def __init__(self, benchmark, serial, command, target_directory, receiver_directory):
        self.benchmark = benchmark
        self.serial = serial
        self.command = command
        self.target_directory = target_directory
        self.receiver_directory = receiver_directory

    def run(self):
        gfx_bench_thread = GFXBench(benchmark=self.benchmark, command=self.command,
                                    serial=self.serial ,target_directory=self.target_directory,
                                    receiver_directory=self.receiver_directory)
        QThreadPool.start(gfx_bench_thread)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
