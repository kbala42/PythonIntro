'''
---------------------------------------------------------tw:@tek_elo
Pencereyi boyutlandırma 2: setGeometry metodunu kullanarak
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # setGeometry(x, y, width, height)
        # x:başlangıç x, y: başlangıç y,
        # width: pencere genişlik, height: pencere yükseklik
        self.setGeometry(50,50,1000, 640)

        self.show()


window = Window()
sys.exit(app.exec_()) # ana döngüyü yürütmek için