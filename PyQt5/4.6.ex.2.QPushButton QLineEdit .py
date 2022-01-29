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


        self.entry()
        self.show()

    def entry(self):
        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("Giriş yapın")
        self.textBox.move(100,50)

        button = QPushButton("Kaydet",self)
        button.move(100,70)
        button.clicked.connect(self.saveFunction)

    def saveFunction(self):
        txt = self.textBox.text()
        mesaj = 'Boş bırakmayın'
        if txt !="":
            print(txt)
        else:
            window.setWindowTitle(mesaj)
            print(mesaj)



app=QApplication([])
window = Window()
app.exec()