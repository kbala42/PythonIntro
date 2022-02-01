'''
---------------------------------------------------------tw:@tek_elo
QListWidget Ekleme
Listeleme yapmamızı sağlayan bileşendir.
--------------------------------------------------------------------
'''
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.listView()
        self.show()

    def listView(self):

        self.list = QListWidget(self)

        yil=2010

        for i in range(20):
            yil += 1
            self.list.addItem(str(yil))




app = QApplication([])
window = Window()
app.exec_()