'''
---------------------------------------------------------tw:@tek_elo
QRadioButton Kullanımı
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

        self.radioButton()
        self.show()

    def radioButton(self):

        self.secim1 = QRadioButton("seçim1",self)
        self.secim2 = QRadioButton("seçim2", self)
        self.secim3 = QRadioButton("seçim3", self)

        self.secim1.move(500, 50)
        self.secim2.move(500, 70)
        self.secim3.move(500, 90)



app = QApplication([])
window = Window()
app.exec_()
