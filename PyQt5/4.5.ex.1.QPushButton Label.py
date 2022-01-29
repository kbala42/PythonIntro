'''
---------------------------------------------------------tw:@tek_elo
Pencereye QPushButton Olay Ekleme
QPushButton QLabel Örneği
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

        self.label()
        self.show()

    def label(self):

        self.text1=QLabel("Merhaba",self)
        text2=QLabel("PyQt5",self)

        self.text1.move(170,50)
        text2.move(170,80)

        button = QPushButton("Değiştir",self)
        button.move(170,100)
        button.clicked.connect(self.buttonFuction)

    def buttonFuction(self):
        self.text1.setText("Merhaba Dünya")
        self.text1.adjustSize()
        print("Merhaba Dünya")




app=QApplication([])
window = Window()
app.exec()