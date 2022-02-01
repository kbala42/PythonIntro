'''
---------------------------------------------------------tw:@tek_elo
QProgressBar Kullanımı
QHBox ekleme ayrı bir fonksiyon içindede yapılabilir
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

        self.horizontal()

        self.show()

    def horizontal(self):

        hbox = QHBoxLayout()

        button1 = QPushButton("yes",self)
        text1 = QLabel("Evet",self)
        button2 = QPushButton("No",self)
        text2 = QLabel("Hayır",self)
        button3 = QPushButton("Continue",self)
        text3 = QLabel("Devam",self)

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