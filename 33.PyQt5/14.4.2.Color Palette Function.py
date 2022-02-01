'''
---------------------------------------------------------tw:@tek_elo
QProgressBar Kullanımı
Renk Palet uygulamasına fonksiyon ekleme
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

        self.sliderKirmizi = QSlider(Qt.Horizontal, self)
        self.sliderYesil = QSlider(Qt.Horizontal, self)
        self.sliderMavi = QSlider(Qt.Horizontal, self)

        self.sliderKirmizi.setGeometry(360,380, 200, 20)
        self.sliderYesil.setGeometry(360,410, 200, 20)
        self.sliderMavi.setGeometry(360,440, 200, 20)

        self.labelKirmiziDeger = QLabel('0',self)
        self.labelYesilDeger = QLabel('0', self)
        self.labelMaviDeger = QLabel('0', self)

        self.labelKirmiziDeger.move(580,380)
        self.labelYesilDeger.move(580,410)
        self.labelMaviDeger.move(580,440)

        self.show()

        #slider başlangıç ve bitiş aralıklarını ayarlıyoruz
        self.sliderKirmizi.setRange(0,255)
        self.sliderYesil.setRange(0,255)
        self.sliderMavi.setRange(0, 255)

        self.sliderKirmizi.valueChanged.connect(self.kirmiziDegistir)
        self.sliderYesil.valueChanged.connect(self.yesilDegistir)
        self.sliderMavi.valueChanged.connect(self.maviDegistir)

    def kirmiziDegistir(self, kirmizi):
        self.labelKirmiziDeger.setText(str(kirmizi))
        self.labelKirmiziDeger.adjustSize()
        self.widget.setStyleSheet('border:1px solid black; background-color: rgb(%d, %d, %d);' % (kirmizi, self.sliderYesil.value(), self.sliderMavi.value()))

    def yesilDegistir(self, yesil):
        self.labelYesilDeger.setText(str(yesil))
        self.labelYesilDeger.adjustSize()
        self.widget.setStyleSheet('border:1px solid black; background-color: rgb(%d, %d, %d);' % ( self.sliderKirmizi.value(), yesil, self.sliderMavi.value()))

    def maviDegistir(self, mavi):
        self.labelMaviDeger.setText(str(mavi))
        self.labelMaviDeger.adjustSize()
        self.widget.setStyleSheet('border:1px solid black; background-color: rgb(%d, %d, %d);' % (
        self.sliderKirmizi.value(), self.sliderYesil.value(), mavi))

app = QApplication([])
window = Window()
app.exec_()