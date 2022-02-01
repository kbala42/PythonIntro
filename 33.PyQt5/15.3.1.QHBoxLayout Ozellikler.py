'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout Özellikler
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

        #Yatay yüzey üretiyoruz
        self.hbox = QHBoxLayout(self)

        self.hbox.addStretch()  # sağ tarafa yasla

        self.hbox.addWidget(QPushButton("Click"))
        self.hbox.addWidget(QLabel("Tıkla"))

        # Boşluk eklemek
        #self.hbox.addSpacing(100)

        self.hbox.addWidget(QPushButton("Accept"))
        self.hbox.addWidget(QLabel("Onay"))

        self.hbox.addWidget(QPushButton("Continue" ))
        self.hbox.addWidget(QLabel("Devam"))

        self.hbox.addStretch()  # sol tarafa yasla
        # sol tarafa ve sağ tarafa aynı anda işletilirse ortaya yaslama olur

        #Boşlukları ayarlama
        self.hbox.setContentsMargins(0,0,0,0)

        #Yerleşim yönü
        #self.hbox.setDirection(QBoxLayout.RightToLeft)

        self.show()


app = QApplication([])
window = Window()
app.exec_()