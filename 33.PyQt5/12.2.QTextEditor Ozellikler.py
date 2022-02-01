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

        self.textEdit = QTextEdit(self)
        
        #Pencerede yazdıracağımız metni giriyoruz
        self.textEdit.setText('Merhaba, bu metin editöründe ilk yazımız')

        #imleç genişliğini ayarlama
        #self.textEdit.setCursorWidth(10)

        # Varsayımda editöre yapıştırma işlemi zengin text editörüdür
        #Yapıştırmada kopyalamadaki biçimlendirmeyi alır. Yalnızca metin
        # istiyorsak false yapacağız
        #self.textEdit.setAcceptRichText(False)



        self.show()


app = QApplication([])
window = Window()
app.exec_()