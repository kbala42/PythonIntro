'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Kenar çzigsini değiştirme
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

        self.table.setGridStyle(Qt.SolidLine)
        #self.table.setGridStyle(Qt.DashLine)
        #self.table.setGridStyle(Qt.DotLine)


        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()