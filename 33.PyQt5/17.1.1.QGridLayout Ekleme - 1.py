'''
---------------------------------------------------------tw:@tek_elo
QGridLayout Ekleme
Izgaralar şeklinde yüzey oluşturup, elemanlar eklemek için kullanıyoruz
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

        self.grid = QGridLayout(self)

        #Sırasıyla 0. satır 0. sütun, 1 satır 1 sütun genişliğinde
        self.grid.addWidget(QLabel('Kırmızı'), 0, 0, 1 ,1)
        self.grid.addWidget(QLabel('Yeşil'), 0, 1, 1, 1)
        self.grid.addWidget(QPushButton('Kırmızı'),1,0,1,1)
        # Sırasıyla 1. satır 1. sütun, 1 satır 1 sütun genişliğinde
        self.grid.addWidget(QPushButton('Yeşil'), 1, 1, 1, 1)

        #Boşluk 0
        #self.grid.setSpacing(0)



        self.show()

app = QApplication([])
window = Window()
app.exec_()