'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Hücreye varsayım Değeri Ekleme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # QTableWidget(satır sayısı, sütun sayısı, parent)
        self.table = QTableWidget(10, 10, self)
        # Tablomuzu boyutlandırıyoruz
        self.table.setGeometry(10,10,500,400)

        #Hücreye varsayım değeri eklemek için
        self.item = QTableWidgetItem()
        #İçeriği set ediyoruz
        self.item.setText('item 1')
        # Hücre seçiyoruz
        self.table.setItem(5,2,self.item)

        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()