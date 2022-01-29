'''
---------------------------------------------------------tw:@tek_elo
QChechBox Kullanımı
Fonksiyon atama
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

        self.checkBox()
        self.show()

    def checkBox(self):
        self.save = QCheckBox(self)
        self.save.setText('Kontrol')
        self.save.move(500,200)

        button = QPushButton("Kaydet",self)
        button.move(500,240)
        button.clicked.connect(self.checkFunction)

    def checkFunction(self):
        if self.save.isChecked():
            print("Kaydet")
        else:
            print("Kaydetme")

app = QApplication([])
window = Window()
app.exec_()