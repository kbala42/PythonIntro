'''
---------------------------------------------------------tw:@tek_elo
QChechBox Kullanımı
Birden fazla seçimim yaptığımızda kullanıyoruz
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

        self.label= QLabel(self)
        self.label.move(500,220)
        self.label.setText('Seçmek istediğiniz dersler')

        self.check1 = QCheckBox('Matematik',self)
        self.check2 = QCheckBox('Fizik',self)
        self.check3 = QCheckBox('Kimya',self)
        self.check4 = QCheckBox('Biyoloji',self)

        self.check1.move(500,250)
        self.check2.move(500,270)
        self.check3.move(500,290)
        self.check4.move(500,310)

        self.check1.toggled.connect(self.kontrol1)

        self.show()

    def kontrol1(self,durum):
        print('Matematik')
        print(durum)

app = QApplication([])
window = Window()
app.exec_()