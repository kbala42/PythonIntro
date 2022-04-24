'''
---------------------------------------------------------tw:@tek_elo
İmaj Ekleme
--------------------------------------------------------------------
'''
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1600, 800)
        self.setWindowTitle("Yalova Nano")

        self.image()
        self.show()

    def image(self):

        self.image = QLabel(self)
        self.image.setPixmap((QPixmap("yalovaNano.PNG")))
        self.image.move(100,100)


app = QApplication([])
window = Window()
app.exec_()