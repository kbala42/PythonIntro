'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Satır ve Sütun gizleme
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

        # 3. satır gizleme
        self.table.setRowHidden(3,True)

        # 3. sütun gizleme
        self.table.setColumnHidden(3,True)


        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()