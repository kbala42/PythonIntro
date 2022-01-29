'''
---------------------------------------------------------tw:@tek_elo
QComboBox Kullanımı
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

        self.comboBox()
        self.show()

    def comboBox(self):

        self.combo = QComboBox(self)
        self.combo.move(500, 200)
        self.combo.addItem("seçim1",self)
        self.combo.addItem("seçim2", self)
        self.combo.addItem("seçim3", self)


        button = QPushButton("Combo Button",self)
        button.move(500,240)
        button.clicked.connect(self.comboFunction)

    def comboFunction(self):
        print(self.combo.currentText())

app = QApplication([])
window = Window()
app.exec_()