'''
---------------------------------------------------------tw:@tek_elo
Pencereyi Konumlandırma 3: setGeometry metodunu kullanarak
Konumlandırmada yine setGeometry metodunun x ve y değerleri kullanılabilir
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
        self.setGeometry(300,200,800, 600)
        # pos() metodu ilede pencerenin konumunu yazdırabiliriz
        print(self.pos())
        # geometry() metodu ilede pencerenin hem konumunu hemde boyutlarını yazdırabiliriz
        print(self.geometry())
        # window.show() metodu yerine kullanıyoruz
        self.show()


window = Window()
sys.exit(app.exec_()) # ana döngüyü yürütmek için