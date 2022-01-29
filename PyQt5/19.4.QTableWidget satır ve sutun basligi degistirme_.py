'''
---------------------------------------------------------tw:@tek_elo
QTable Widget Kullanımı
Satır ve Sütun Başlığı Değiştirmek
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

        #Satır başlıklarını değiştiriyoruz
        self.table.setVerticalHeaderLabels(['Satır 1', 'Satır 2', 'Satır 3'])

        #Sütun başlıklarını değiştiriyoruz
        self.table.setHorizontalHeaderLabels(['Sütun 1', 'Sütun 2', 'Sütun 3'])


        self.resize(800, 640)
        self.show()

app = QApplication([])
window = Window()
app.exec_()