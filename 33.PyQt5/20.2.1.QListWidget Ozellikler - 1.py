'''
---------------------------------------------------------tw:@tek_elo
QListWidget Özellikler 1
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


        #Eleman sayını yazdırma
        print(self.list.count())

        # Yeni eleman ekleyerek seçili olmasını sağlamak
        #self.item = QListWidgetItem('Yeni Eleman', self.list)
        #self.list.setCurrentItem(self.item)

        #Satırı belirleyerek seçili hale getirme
        self.list.setCurrentRow(4)

        # seçili elemanı belirleme ve yazdırma
        secim = self.list.currentItem().text()
        print(secim)

        #Sıralama artan - varsayım
        #self.list.sortItems(Qt.AscendingOrder)

        # Sıralama azalan
        #self.list.sortItems(Qt.DescendingOrder)

        #Elaman değiştirme
        # degisecek = self.list.takeItem(3)
        # print(degisecek.text())
        # degisecek.setText('Değişen Elaman')
        # self.list.insertItem(3,degisecek)

        #Listeyi temizleme
        #self.list.clear()



        self.show()

app = QApplication([])
window = Window()
app.exec_()