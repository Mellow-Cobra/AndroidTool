

# Standard Imports
import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QWidget, QPushButton, QMainWindow, QApplication, QGridLayout, \
    QTabWidget
from PyQt5.QtCore import Qt, QRunnable, QThreadPool

# Android Tool Imports
from androidbenchmarktool.routines.gfx_bench_routine import GFXBench
s
class MainWindow(QWidget):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("androidbenchmarktool")
        self.setGeometry(500, 500, 500, 500)

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
        self.manahattan_311 = QPushButton("Manhattan 3.1")
        self.manahattan_311.clicked.connect(self.onclick_manhattan_311)
        self.aztec_ruins_open_gl = QPushButton("Aztec Ruins")
        gfx_bench_layout.addWidget(self.manahattan_311)
        gfx_bench_layout.addWidget(self.aztec_ruins_open_gl)

        # Antutu AI Benchmark
        ai_benchmark_layout = QVBoxLayout()
        self.ai_antutu = QPushButton("Run Antutu AI")
        ai_benchmark_layout.addWidget(self.ai_antutu)

        self.benchmark_tab.layout.addLayout(gfx_bench_layout)
        self.benchmark_tab.layout.addLayout(ai_benchmark_layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    def onclick_manhattan_311(self):
        """Event handler for benchmark manhattan"""
        ManhattanGL("Manhattan")


class ManhattanGL(QRunnable):
    """Thread class used to run benchmark application"""

    def __init__(self, benchmark, serial, command, target_directory, reciever_directory):
        self.benchmark = benchmark
        self.serial = serial
        self.command = command
        self.target_directory = target_directory
        self.reciever_directory = reciever_directory

    def run(self):
        gfx_bench_thread = GFXBench(benchmark=self.benchmark, command=self.command,
                                    serial=self.serial,target_directory=self.target_directory,
                                    reciever_directory=self.reciever_directory)
        QThreadPool.start(gfx_bench_thread)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()