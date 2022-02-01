'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout Ekleme
QHBoxLayout yatay yüzey oluşturup, elemanlar eklemek için kullanıyoruz
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

        #Yatay yüzey üretiyoruz
        self.hbox = QHBoxLayout(self)

        #hbox'ın görünür hale getirmek için eleman eklemeliyiz
        #buton ve etiket ekliyeceğiz
        self.button1 = QPushButton("Click")
        self.label1 = QLabel("Tıkla")

        #Bunuda widget ekliyerek yapıyoruz
        #Ekleme sırasına göre görünümde değişir
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.label1)

        #Eklemek için diğer yöntem elemanı widget eklemektir
        self.hbox.addWidget(QPushButton("Accept"))
        self.hbox.addWidget(QLabel("Onay"))

        #Eleman eklendikçe hbox eleman genişliklerini otomatikman ayarlar
        self.hbox.addWidget(QPushButton("Continue" ))
        self.hbox.addWidget(QLabel("Devam"))


        self.show()



app = QApplication([])
window = Window()
app.exec_()