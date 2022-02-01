'''
---------------------------------------------------------tw:@tek_elo
QTextEditor Kullanımı
Metin girişi ve düzenlemesi için kullanıyoruz
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

        self.progressBar()
        self.show()

    def progressBar(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(400,40,200,25)
        self.pbar.setValue(0)

        # Zamanlama için timer kullanıyoruz
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        #0.5s aralıklarla işlem yaptıracağız
        self.timer.start(500)

    def handleTimer(self):
        value = self.pbar.value()
        step = 5
        if value<100:# 100 den küçük olduğu sürece değeri 5 arttır
            value=value+step
            self.pbar.setValue(value)
        else:
            self.timer.stop()

app = QApplication([])
window = Window()
app.exec_()