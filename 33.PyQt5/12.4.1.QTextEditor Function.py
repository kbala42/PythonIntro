'''
---------------------------------------------------------tw:@tek_elo
QTextEditor Kullanımı
Fonksiyon ekleme
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

        self.textEdit = QTextEdit(self)
        #Pencerede yazdıracağımız metni giriyoruz
        self.textEdit.setText('Merhaba, bu metin editöründe ilk yazımız')

        #Giriş butonunu tanımlıyoruz ve fonksiyon bağlıyoruz
        self.button = QPushButton('Giriş',self)
        self.button.clicked.connect(self.giris)
        self.button.move(300,450)

        self.show()

    def giris(self):
        #HTML giriş
        #self.textEdit.insertHtml('<b>HTML Giriş</b> ')
        # Plain text giriş
        #self.textEdit.insertPlainText('<b>HTML Giriş</b> ')
        # İşaretli kısmın Fontunu ve boyunu seçme
        self.textEdit.setFontFamily('Arial')
        self.textEdit.setFontPointSize(20)

app = QApplication([])
window = Window()
app.exec_()