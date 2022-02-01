'''
---------------------------------------------------------tw:@tek_elo
QGridLayout Ekleme 3
Fonksiyon kullanarak
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.gridLayout()
        self.show()

    def gridLayout(self):

        grid = QGridLayout()

        grid.addWidget(QPushButton('Buton  1'), 0, 0)
        grid.addWidget(QPushButton('Buton  2'), 1, 0)
        grid.addWidget(QPushButton('Buton  3'), 0, 1)
        grid.addWidget(QPushButton('Buton  4'), 1, 1)

        self.setLayout(grid)


app = QApplication([])
window = Window()
app.exec_()