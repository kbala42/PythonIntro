'''
---------------------------------------------------------tw:@tek_elo
QGridLayout Ekleme
Döngü kullanarak
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

        for i in range(5):
            for j in range(5):
                self.grid.addWidget(QLabel('Hücre'),i,j,1,1)

        #Boşluk 0
        #self.grid.setSpacing(0)



        self.show()

app = QApplication([])
window = Window()
app.exec_()