'''
---------------------------------------------------------tw:@tek_elo
Pencereye message question
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

        button = QPushButton("Mesaj",self)
        button.move(100,70)
        button.clicked.connect(self.mesajFonksiyonu)

    def mesajFonksiyonu(self):
        mBox=QMessageBox.question(self,"Soru","Hava güzel mi?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Cancel)

        if mBox == QMessageBox.Yes:
            print("Evet")
        elif mBox == QMessageBox.No:
            print("Hayır")
        else:
            print("Vazgeçtiniz")


app=QApplication([])
window = Window()
app.exec()