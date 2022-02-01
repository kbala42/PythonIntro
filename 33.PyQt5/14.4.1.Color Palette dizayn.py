'''
---------------------------------------------------------tw:@tek_elo
QProgressBar Kullanımı
Renk Palet uygulaması tasarımı
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle('Renk Palet Uygulaması')

        self.widget = QWidget(self)
        self.widget.setGeometry(300,50, 300, 300)
        self.widget.setStyleSheet('border:1px solid black; background-color: lightgray;')

        self.labelKirmizi = QLabel('Kirmizi',self)
        self.labelYesil = QLabel('Yeşil', self)
        self.labelMavi = QLabel('Mavi', self)

        self.labelKirmizi.move(320,380)
        self.labelYesil.move(320,410)
        self.labelMavi.move(320,440)

        self.sliderKrimizi = QSlider(Qt.Horizontal, self)
        self.sliderYesil = QSlider(Qt.Horizontal, self)
        self.sliderMavi = QSlider(Qt.Horizontal, self)

        self.sliderKrimizi.setGeometry(360,380, 200, 20)
        self.sliderYesil.setGeometry(360,410, 200, 20)
        self.sliderMavi.setGeometry(360,440, 200, 20)

        self.labelKirmiziDeger = QLabel('0',self)
        self.labelYesilDeger = QLabel('0', self)
        self.labelMaviDeger = QLabel('0', self)

        self.labelKirmiziDeger.move(580,380)
        self.labelYesilDeger.move(580,410)
        self.labelMaviDeger.move(580,440)

        self.show()





app = QApplication([])
window = Window()
app.exec_()