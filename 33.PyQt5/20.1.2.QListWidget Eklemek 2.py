'''
---------------------------------------------------------tw:@tek_elo
QListWidget Ekleme 2
item şeklinde
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

        self.list.addItem('Eleman 1')
        #Liste şeklinde eklenti yapabiliriz
        self.list.addItems(['Eleman 2','Eleman 3'])
        #liste değişkeni
        liste1 = ['Eleman 4','Eleman 5','Eleman 6']
        self.list.addItems(liste1)

        self.item = QListWidgetItem('Eleman 7', self.list)
        self.item2 = QListWidgetItem()
        self.item2.setText('Elaman 8')
        self.list.addItem(self.item2)

        #Araya girme
        self.list.insertItem(3,'Yeni Eleman')





        self.show()

app = QApplication([])
window = Window()
app.exec_()