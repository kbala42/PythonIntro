'''
---------------------------------------------------------tw:@tek_elo
QComboBox Kullanımı
QRadio ile birlikte kullanımı
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

dicSiniflar = {
    'Sinif10':['Bidevdi','Esalar'],
    'Sinfi11':['EKAA','BDU']
}
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.combo = QComboBox(self)
        self.combo.setGeometry(100,100, 120, 20)

        self.radio1 = QRadioButton('Sinif10',self)
        self.radio1.move(100, 80)
        self.radio2 = QRadioButton('Sinif11', self)
        self.radio2.move(200, 80)

        self.radio1.clicked.connect(self.listing)
        self.radio2.clicked.connect(self.listing)

        self.show()

    def listing(self):
        if self.radio1.isChecked():
            self.combo.clear()
            self.combo.addItems(dicSiniflar['Sinif10'])

        if self.radio2.isChecked():
            self.combo.clear()
            self.combo.addItems(dicSiniflar['Sinfi11'])

app = QApplication([])
window = Window()
app.exec_()