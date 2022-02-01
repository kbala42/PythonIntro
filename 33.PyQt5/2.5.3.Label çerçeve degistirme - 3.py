'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label Çerçeve Değiştirme - 1
Çerçeve metin silme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
# QFont için
from PyQt5.QtGui import *
# label metin konumlandırma için
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('LABEL', self)
        self.label.setText('yeni label')
        self.label.move(100,100)
        # str: Font, 18: Font boyutu, 100:Font kalınlığı, True: italic (varsayında false)
        self.setFont(QFont('Verdana', 18, 100, True ))

        # Çerçeve şekli
        self.label.setFrameShape(QFrame.Box)
        #Çerçeve kalınlık
        self.label.setLineWidth(12)
        #Çerçeve boyut
        self.label.resize(400,300)
        # Çerçeve metin içeriğini temizleme
        self.label.clear()




        self.resize(800, 640)
        self.setWindowTitle("PyQt5 Label")
        self.show()


app=QApplication([])
window = Window()
app.exec()