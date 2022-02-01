'''
---------------------------------------------------------tw:@tek_elo
QSlider Özellikleri
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


        # Aralık belirleme
        self.slider.setRange(0,100)
        # Başlangıç belirleme
        self.slider.setValue(50)
        # Yöne değiştirme. Doğru çalışabilmesi için
        # en ve boy'da ayarlanması gerekir
        self.slider.setOrientation(Qt.Vertical)
        self.slider.setGeometry(50, 50, 20, 300)
        # İzleme çizgileri
        self.slider.setTickPosition(QSlider.TicksBothSides)
        #Çizgi aralıkları
        self.slider.setTickInterval(20)


        self.show()




app = QApplication([])
window = Window()
app.exec_()