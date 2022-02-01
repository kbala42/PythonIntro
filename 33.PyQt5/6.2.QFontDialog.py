'''
---------------------------------------------------------tw:@tek_elo
6.2.QFFontDialog Kullanımı

--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.label = QLabel('Font Değiştirme',self)
        self.label.move(400,200)

        self.button = QPushButton('Font Ayarla',self)
        self.button.clicked.connect(self.fontDegistir)

        self.show()

    def fontDegistir(self):
        font, ok =QFontDialog.getFont()

        if ok:
            self.label.setFont(font)
            self.label.adjustSize()


app = QApplication([])
window = Window()
app.exec_()




