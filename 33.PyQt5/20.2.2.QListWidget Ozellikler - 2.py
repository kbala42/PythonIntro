'''
---------------------------------------------------------tw:@tek_elo
QListWidget Özellikler 2

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

        #Eleman gizleme
        #self.list.setRowHidden(3,True)

        # Görünüm değiştirme sağdan sola
        #self.list.setFlow(QListView.LeftToRight)

        # self.list.setViewMode(QListWidget.IconMode)
        self.item = QListWidgetItem('Yeni',self.list)
        self.item.setIcon(QIcon('buton.PNG'))
        self.list.setViewMode(QListWidget.IconMode)
        #List moda geçiş
        #self.list.setViewMode(QListWidget.ListMode)



        self.show()

app = QApplication([])
window = Window()
app.exec_()