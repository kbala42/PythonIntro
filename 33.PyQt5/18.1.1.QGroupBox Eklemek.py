'''
---------------------------------------------------------tw:@tek_elo
QGroupBox Ekleme
Elamanları gruplayarak toplu işlem yapabilemesini sağlayan bileşendir
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

        self.group = QGroupBox(self)
        self.group.setTitle('Tercihleriniz (İsteğe Bağlı)')
        self.group.setGeometry(50,50,300,400)
        #Grup yazısını sola yaslıyoruz
        self.group.setAlignment(Qt.AlignLeft)
        # Grup tikli
        self.group.setCheckable(True)
        # Grup tiksiz
        #self.group.setCheckable(False)

        self.show()

app = QApplication([])
window = Window()
app.exec_()