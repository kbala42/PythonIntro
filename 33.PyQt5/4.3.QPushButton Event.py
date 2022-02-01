'''
---------------------------------------------------------tw:@tek_elo
Pencereye QPushButton Olay Ekleme
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

        self.button()
        self.show()

    def button(self):
        button = QPushButton("Merhaba",self)
        #Butonuna ipucu verme
        button.setToolTip("PyQt5 butonu")
        button.resize(120,100)
        #Buton konum ayarlama
        button.move(50,50)
        # Buton fontunu ayarlama
        button.setFont(QFont('Verdana', 16))
        button.clicked.connect(self.buttonFuction)

    def buttonFuction(self):
        selam = 'Merhaba'
        # selam yazısını pencere başlığına ve komut satırına çıkış alıyoruz
        window.setWindowTitle(selam)
        print(selam)




app=QApplication([])
window = Window()
app.exec()