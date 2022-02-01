'''
---------------------------------------------------------tw:@tek_elo
QVBoxLayout Ekleme
QHBoxLayout dikey yüzey oluşturup, elemanlar eklemek için kullanıyoruz
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

        #Dikey yüzey üretiyoruz
        self.vbox = QVBoxLayout(self)

        #vbox'ın görünür hale getirmek için eleman eklemeliyiz
        #buton ve etiket ekliyeceğiz
        self.button1 = QPushButton("Click")
        self.label1 = QLabel("Tıkla")

        #Bunuda widget ekliyerek yapıyoruz
        #Ekleme sırasına göre görünümde değişir
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.label1)

        #Eklemek için diğer yöntem elemanı widget eklemektir
        self.vbox.addWidget(QPushButton("Accept"))
        self.vbox.addWidget(QLabel("Onay"))
        
        #Eleman eklendikçe vbox eleman genişliklerini otomatikman ayarlar
        self.vbox.addWidget(QPushButton("Continue" ))
        self.vbox.addWidget(QLabel("Devam"))


        self.show()

    def horizontal(self):



        hbox.addWidget(button1)
        hbox.addWidget(text1)
        hbox.addWidget(button2)
        hbox.addWidget(text2)
        hbox.addWidget(button3)
        hbox.addWidget(text3)


        self.setLayout(hbox)

app = QApplication([])
window = Window()
app.exec_()