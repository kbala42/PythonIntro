'''
---------------------------------------------------------tw:@tek_elo
QToolButton Kullanımı
ikon kullanmak
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
        self.tbutton.setIconSize(QSize(120,120))
        #Yazı eklemek
        self.tbutton.setText('Dur')
        # Yazı altında isteniyorsa
        self.tbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #ipucu
        self.tbutton.setToolTip('Durdur')
        #ipucu bekleme süresini belirlemek 3000ms:3s
        self.tbutton.setToolTipDuration(3000)



        self.show()



app = QApplication([])
window = Window()
app.exec_()




