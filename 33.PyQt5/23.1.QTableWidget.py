'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Tablo oluşturma
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # QTableWidget(satır sayısı, sütun sayısı, parent)
        self.table = QTableWidget(10, 10, self)
        # Tablomuzu boyutlandırıyoruz
        self.table.setGeometry(20,20,400,400)

        #Satır sayısını öğrenmek istersek
        print('Satır sayısı: ',self.table.rowCount())
        # sütun sayısını öğrenmek istersek
        print('Sütun sayısı: ',self.table.columnCount())



        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()