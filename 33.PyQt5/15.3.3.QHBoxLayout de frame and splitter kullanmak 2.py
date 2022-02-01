'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout de frame and splitter kullanmak 2
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

        self.formLayout()
        self.show()

    def formLayout(self):

        hbox1 = QHBoxLayout()

        hbox1.addWidget(QPushButton("1"))
        hbox1.addWidget(QPushButton("2"))
        hbox1.addStretch()

        formLayout=QFormLayout()
        formLayout.addRow(QLabel("1 yada 2 ye basın"),hbox1)

        self.setLayout(formLayout)


app = QApplication([])
window = Window()
app.exec_()