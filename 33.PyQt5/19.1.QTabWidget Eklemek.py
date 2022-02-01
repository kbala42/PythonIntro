'''
---------------------------------------------------------tw:@tek_elo
QTabWidget Ekleme
Sekmelerle işlem yapmamızı sağlayan bileşendir.
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

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(50,50, 900, 550)

        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.widget3 = QWidget()

        self.tabWidget.addTab(self.widget1, QIcon('buton.PNG'),'Sekme 1')
        self.tabWidget.addTab(self.widget2, QIcon('buton.PNG'),'Sekme 2')
        self.tabWidget.addTab(self.widget3, QIcon('buton.PNG'),'Sekme 3')




        self.show()

app = QApplication([])
window = Window()
app.exec_()