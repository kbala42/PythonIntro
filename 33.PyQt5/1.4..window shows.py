'''
---------------------------------------------------------tw:@tek_elo
Pencerenin minimum boyutta, maksimum boyut yada
sabit boyutta olması sağlanabilir
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        # Pencerenin alabileceği minimum boyut belirlenebilir
        #self.setMinimumSize(300,300)
        # Pencerenin alabileceği maksimum boyut belirlenebilir
        #self.setMaximumSize(900, 900)
        # Pencerenin boyutu sabit olarak belirlenebilir
        #self.setFixedSize(500, 500)

        self.show()

window = Window()
sys.exit(app.exec_()) # ana döngüyü yürütmek için