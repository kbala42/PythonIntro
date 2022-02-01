'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Satır ve Sütun'un Genişlik ve Yüksekliğini Ayarlama
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

        # 1. satır yüksekliğini 100 yapma
        self.table.setRowHeight(1,100)

        # 1. sütun genişliğini 100 yapma
        self.table.setColumnWidth(1,100)


        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()