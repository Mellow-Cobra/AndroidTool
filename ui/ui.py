

# Standard Imports
import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QWidget, QPushButton, QMainWindow, QApplication, QGridLayout
from PyQt5.QtCore import Qt, QRunnable, QThreadPool

# Android Tool Imports
from anroidbenchmarktool.routines.gfx_bench_routine import Manhattan
s
class MainWindow(QWidget):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("androidbenchmarktool")
        self.setGeometry(500, 500, 500, 500)

        main_layout = QGridLayout()

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

        main_layout.addLayout(gfx_bench_layout, 0, 1)
        main_layout.addLayout(ai_benchmark_layout, 0 , 0)

        self.setLayout(main_layout)

    def onclick_manhattan_311(self):
        """Event handler for benchmark manhattan"""
        ManhattanGL("Manhattan")


class ManhattanGL(QRunnable):
    """Thread class used to run benchmark application"""

    def __init__(self, benchmark):
        self.benchmark = benchmark

    def run(self):
        manhattan_thread_routine = ManhattanGL(benchmark=self.benchmark)
        QThreadPool.start(manhattan_thread_routine)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()