'''
---------------------------------------------------------tw:@tek_elo
QToolButton Kullanımı
QToolButton ikon ve metinlerle yapılan buton türü
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("QToolButton Kullanımı")

        # Buton üretiyoruz
        self.tbutton = QToolButton(self)
        #Butonun yerini ve boyutlarını seçiyoruz
        self.tbutton.setGeometry(100,100,120, 120)
        #İkonu seçiyoruz
        self.tbutton.setIcon(QIcon('buton.PNG'))
        self.tbutton.setIconSize(QSize(80,80))
        #Yazı eklemek
        self.tbutton.setText('Dur')
        # Yazı yanında isteniyorsa
        #self.tbutton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # Yazı altında isteniyorsa
        self.tbutton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)



        self.show()



app = QApplication([])
window = Window()
app.exec_()




