'''
---------------------------------------------------------tw:@tek_elo
QGroupBox vbox toggle kullanımı
--------------------------------------------------------------------
'''
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.group = QGroupBox(self)
        self.group.setTitle('Tercihleriniz (İsteğe Bağlı)')
        self.group.setGeometry(50,50,300,400)
        #Grup yazısını sola yaslıyoruz
        self.group.setAlignment(Qt.AlignLeft)
        # Grup tikli
        self.group.setCheckable(True)

        # vbox üretiyoruz
        self.vbox = QVBoxLayout()
        # check kutularını üretiyoruz
        self.onay1 = QCheckBox('Onay 1')
        self.onay2 = QCheckBox('Onay 2')
        self.onay3 = QCheckBox('Onay 3')
        #vbox'a onay kutularını ekliyoruz
        self.vbox.addWidget(self.onay1)
        self.vbox.addWidget(self.onay2)
        self.vbox.addWidget(self.onay3)

        #grup kutusuna vbox ekliyoruz
        self.group.setLayout(self.vbox)

        self.show()

        self.group.toggled.connect(self.degistir)

    def degistir(self, d):
        if d:
            self.onay1.setChecked(True)
            self.onay2.setChecked(True)
            self.onay3.setChecked(True)
        else:
            self.onay1.setChecked(False)
            self.onay2.setChecked(False)
            self.onay3.setChecked(False)

app = QApplication([])
window = Window()
app.exec_()