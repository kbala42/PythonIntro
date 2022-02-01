'''
---------------------------------------------------------tw:@tek_elo
QProgressBar Kullanımı
Proses takibi için kullandığımız bileşen
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

        self.slider()
        self.show()

    def slider(self):

        vbox =QVBoxLayout()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        
        self.slider.valueChanged.connect(self.sliderFunction)
        
        vbox.addWidget(self.slider)
        vbox.addStretch()
        self.setLayout(vbox)

    def sliderFunction(self):
        print(self.slider.value())




app = QApplication([])
window = Window()
app.exec_()