'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Hücre Birleştirme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # QTableWidget(satır sayısı, sütun sayısı, parent)
        self.table = QTableWidget(10, 10, self)
        # Tablomuzu boyutlandırıyoruz
        self.table.setGeometry(10,10,500,400)

        # Başlangıç ve bitiş hücreleri veriyoruz
        self.table.setSpan(1,1,2,3)


        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()