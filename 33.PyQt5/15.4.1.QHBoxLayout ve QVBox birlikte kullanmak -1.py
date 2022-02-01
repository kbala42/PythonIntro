'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout ve QVBoxLayout Kullanımı - 1
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

        #Eklemek için diğer yöntem elemanı widget eklemektir
        self.hbox.addWidget(QPushButton("Click"))
        self.hbox.addWidget(QLabel("Tıkla"))
        self.hbox.addWidget(QPushButton("Accept"))
        self.hbox.addWidget(QLabel("Onay"))

        #vbox eklemek
        self.vbox = QVBoxLayout()
        self.hbox.addLayout(self.vbox)

        self.vbox.addWidget(QPushButton("Continue" ))
        self.vbox.addWidget(QLabel("Devam"))

        self.vbox.addWidget(QPushButton("Cancel" ))
        self.vbox.addWidget(QLabel("Vazgeç"))

        self.show()

    def horizontal(self):



        hbox.addWidget(button1)
        hbox.addWidget(text1)
        hbox.addWidget(button2)
        hbox.addWidget(text2)
        hbox.addWidget(button3)
        hbox.addWidget(text3)


        self.setLayout(hbox)

app = QApplication([])
window = Window()
app.exec_()