'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Hücre Odaklanma
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # QTableWidget(satır sayısı, sütun sayısı, parent)
        self.table = QTableWidget(10, 10, self)
        # Tablomuzu boyutlandırıyoruz
        self.table.setGeometry(10,10,500,400)

        # setCurrentCell metodu kullanarak
        #self.table.setCurrentCell(2,2)

        #item'larla odaklanmak
        self.item = QTableWidgetItem()
        #self.item.setText('ITEM')
        self.table.setItem(4,3, self.item)
        self.table.setCurrentItem(self.item)

        #Odak hücresini öğrenmek
        print(self.table.currentItem().text())

        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()