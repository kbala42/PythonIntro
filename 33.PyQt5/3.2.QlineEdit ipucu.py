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

        #ipucu yazısı gözüküyor
        self.line.setPlaceholderText('Kullanıcı adı: ')
        self.line.move(200,300)

        #Clear buton; içerik temizleme butonu, yalnızca içeri yazı girildiğinde aktif olur
        #self.line.setClearButtonEnabled(True)

        # Sadece okunur yapma
        # self.line.setReadOnly(True)

        #Çerçeve kaldırma
        #self.line.setFrame(False)

        #Max. karakter sayısı
        self.line.setMaxLength(8)






        self.show()

app = QApplication([])
window = Window()
app.exec_()
