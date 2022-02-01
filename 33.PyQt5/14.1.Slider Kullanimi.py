'''
---------------------------------------------------------tw:@tek_elo
QSlider Üretimi
Kullanıcının konumlandırmasına göre çıkış veren bileşen
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
        #Slider nesnemizi yatay olarak üretiyoruz
        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.setGeometry(50,50, 300, 20)


        self.show()




app = QApplication([])
window = Window()
app.exec_()