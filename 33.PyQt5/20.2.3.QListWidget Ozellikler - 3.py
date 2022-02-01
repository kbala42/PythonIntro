'''
---------------------------------------------------------tw:@tek_elo
QListWidget Özellikler 3
Klonlama ile listeye ekleme
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

        #Liste elemanımızı üretiyoruz
        self.list = QListWidget(self)
        self.list.setGeometry(50,50,200,400)

        liste1 = ['Eleman 1','Eleman 2','Eleman 3','Eleman 4','Eleman 5','Eleman 6']
        self.list.addItems(liste1)

        self.item = QListWidgetItem('Yeni',self.list)
        for i in range(30):
            self.list.addItem(self.item.clone())
        #Listeyi yanlamasına uzatma
        #self.list.setWrapping(True)


        self.show()

app = QApplication([])
window = Window()
app.exec_()