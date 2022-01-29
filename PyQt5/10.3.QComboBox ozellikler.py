'''
---------------------------------------------------------tw:@tek_elo
QComboBox Kullanımı
Özellikler
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


        self.combo = QComboBox(self)
        self.combo.move(500, 200)
        self.combo.addItem("seçim1",self)
        self.combo.addItem("seçim2", self)
        self.combo.addItem("seçim3", self)
        self.combo.addItems(["seçim4", "seçim5"])

        #1. indisli elemanı silmek
        # self.combo.removeItem(1)

        # içeriği yazdırmak
        print(self.combo.itemText(3))

        # içeriği değiştirmek
        self.combo.setItemText(1, 'Matematik')
        # içeriğe ikon eklemek
        self.combo.setItemIcon(1,QIcon('buton.PNG'))


        self.show()


app = QApplication([])
window = Window()
app.exec_()