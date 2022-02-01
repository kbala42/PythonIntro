'''
---------------------------------------------------------tw:@tek_elo
QProgressBar Kullanımı
Proses takibi için kullandığımız bileşen
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(400, 40, 200, 25)
        # Başlangıç değeri giriyoruz
        self.pbar.setValue(0)

        self.show()






app = QApplication([])
window = Window()
app.exec_()