'''
---------------------------------------------------------tw:@tek_elo
QRadioButton Kullanımı
seçeneklerden yalnızca birisini seçmek için kullanılan buton türüdür
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

        self.secim1.setChecked(True)

        button = QPushButton("Radio Button",self)
        button.move(500,110)
        button.clicked.connect(self.radioButtonFunction)

    def radioButtonFunction(self):

        if self.secim1.isChecked():
            print("seçim1")
        elif self.secim2.isChecked():
            print("seçim2")
        elif self.secim3.isChecked():
            print("seçim3")
        else:
            print("Seçiniz")




app = QApplication([])
window = Window()
app.exec_()