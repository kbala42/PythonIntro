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

        self.tabs()
        self.show()

    def tabs(self):

        mainLayout = QVBoxLayout()

        self.tab = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        vbox = QVBoxLayout()
        hbox1= QHBoxLayout()
        hbox2= QHBoxLayout()

        self.button1 = QPushButton("Birinci Sekme")
        self.button2 = QPushButton("İkinci Sekme")
        self.button3 = QPushButton("Üçüncü Sekme")

        vbox.addWidget(self.button1)
        hbox1.addWidget(self.button2)
        hbox2.addWidget(self.button3)

        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox1)
        self.tab3.setLayout(hbox2)

        self.tab.addTab(self.tab1, "Birinci")
        self.tab.addTab(self.tab2, "İkinci")
        self.tab.addTab(self.tab3, "Üçüncü")

        mainLayout.addWidget(self.tab)

        self.setLayout(mainLayout)


app = QApplication([])
window = Window()
app.exec_()