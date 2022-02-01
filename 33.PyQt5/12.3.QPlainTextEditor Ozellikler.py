'''
---------------------------------------------------------tw:@tek_elo
QPlainTextEditor Kullanımı
Yalnızca Metin girişi ve düzenlemesi için kullanıyoruz
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

        # Düz metin girmek için kullanıyoruz
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.move(500,0)

        # Pencerede yazdıracağımız metni giriyoruz
        self.plainTextEdit.setPlainText('Merhaba, bu metin editöründe ilk yazımız')



        self.show()


app = QApplication([])
window = Window()
app.exec_()