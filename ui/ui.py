

# Standard Imports
import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QWidget, QPushButton, QMainWindow, QApplication, QGridLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("Android Benchmark Tool")
        self.setGeometry(500, 500, 500, 500)

        main_layout = QGridLayout()

        # GFX Bench Control Sub Panel Layout
        gfx_bench_layout = QVBoxLayout()
        self.manahattan_311 = QPushButton("Manhattan 3.1")
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

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()