'''
---------------------------------------------------------tw:@tek_elo
QToolButton Kullanımı
Hazır buton şekli kullanmak
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
        #sağ ok ekliyoruz
        self.tbutton.setArrowType(Qt.RightArrow)
        #oka açılır menü ekliyoruz
        self.tbutton.setPopupMode((QToolButton.MenuButtonPopup))
        self.action = QAction('Copy')
        self.tbutton.addAction(self.action)
        self.action.setShortcut('Ctrl+C')




        self.show()



app = QApplication([])
window = Window()
app.exec_()




