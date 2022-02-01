'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout ve QVBoxLayout Kullanımı - 2
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

        self.verticalAndHorizontal()
        self.show()

    def verticalAndHorizontal(self):

        mainLayout =QHBoxLayout()

        leftLayout  = QVBoxLayout()
        midLayout   = QVBoxLayout()
        rightLayout = QVBoxLayout()

        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(midLayout)
        mainLayout.addLayout(rightLayout)

        button1 = QPushButton("Left")
        button2 = QPushButton("Middle")
        button3 = QPushButton("Right1")
        button4 = QPushButton("Right4")

        leftLayout.addWidget(button1)

        midLayout.addWidget(button2)

        rightLayout.addStretch()
        rightLayout.addWidget(button3)
        rightLayout.addWidget(button4)
        rightLayout.addStretch()

        self.setLayout(mainLayout)

app = QApplication([])
window = Window()
app.exec_()