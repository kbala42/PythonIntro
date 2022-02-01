'''
---------------------------------------------------------tw:@tek_elo
Pencereye message information
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


        self.messageBox()
        self.show()

    def messageBox(self):

        button = QPushButton("Bilgi",self)
        button.move(100,70)
        button.clicked.connect(self.mesajFonksiyonu)

    def mesajFonksiyonu(self):
        mBox=QMessageBox.information(self,"Bilgi","Hava çok güzel!")


app=QApplication([])
window = Window()
app.exec()