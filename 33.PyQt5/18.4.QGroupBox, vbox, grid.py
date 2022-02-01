'''
---------------------------------------------------------tw:@tek_elo
QGroupBox vbox ve grid kullanımı
--------------------------------------------------------------------
'''
import PyQt5.QtCore
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

    def createButton(self):

        groupBox = QGroupBox("Buttons")

        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")

        vbox= QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()


        groupBox.setLayout(vbox)


        return groupBox

    def gridLayout(self):

        grid = QGridLayout()

        grid.addWidget(self.createButton(), 0, 0)
        grid.addWidget(self.createButton(), 1, 0)


        self.setLayout(grid)


app = QApplication([])
window = Window()
app.exec_()