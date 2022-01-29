'''
---------------------------------------------------------tw:@tek_elo
QRadioButton Kullanımı
Birden fazla seçim grubu varsa widget kullanıyoruz
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

        self.secim1 = QRadioButton("seçim1",self)
        self.secim2 = QRadioButton("seçim2", self)
        self.secim3 = QRadioButton("seçim3", self)

        self.secim1.move(500, 50)
        self.secim2.move(500, 70)
        self.secim3.move(500, 90)

        self.widget = QWidget(self)
        self.widget.setGeometry(500, 150, 200, 200)

        self.secim4 = QRadioButton("seçim4", self.widget)
        self.secim5 = QRadioButton("seçim5", self.widget)
        #Bağıl konum. widget içinde konumlandırıyoruz
        self.secim4.move(0, 0)
        # Bağıl konum. widget içinde konumlandırıyoruz
        self.secim5.move(0, 20)

        self.show()


app = QApplication([])
window = Window()
app.exec_()
