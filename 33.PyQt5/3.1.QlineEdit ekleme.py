'''
---------------------------------------------------------tw:@tek_elo
QLineEdit Ekleme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        #QlineEdit ekliyoruz
        self.line = QLineEdit(self)
        # Metin kısmını QLineEdit değiştiriyoruz
        self.line.setText('QLineEdit')
        # 200, 300 taşıyoruz
        self.line.move(200,300)
        #metin kısmını yazdırıyoruz
        print(self.line.text())




        self.show()

app = QApplication([])
window = Window()
app.exec_()
