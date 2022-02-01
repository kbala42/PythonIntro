'''
---------------------------------------------------------tw:@tek_elo
QFontComboBox Kullanımı
Açılır Font seçim yapmak iiçin kullanıyoruz
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

        self.label = QLabel('Font Deneme',self)
        self.label.move(100,100)

        self.comboFont = QFontComboBox(self)
        self.comboFont.currentFontChanged.connect(self.labelFont)
        self.comboFont.move(200,100)

        self.show()

    def labelFont(self, font):
        self.label.setFont(font)
        self.label.adjustSize()


app = QApplication([])
window = Window()
app.exec_()