'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Tablonun satır ve sütun sayılarını değiştirme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # QTableWidget(satır sayısı, sütun sayısı, parent)
        self.table = QTableWidget(10, 10, self)
        # Tablomuzu boyutlandırıyoruz
        self.table.setGeometry(20,20,500,400)

        #Tablonun satır sayısını değiştirme
        self.table.setRowCount(20)
        #Tablonun sütun sayısını değiştirme
        self.table.setColumnCount(15)

        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()