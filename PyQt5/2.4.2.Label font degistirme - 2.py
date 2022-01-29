'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label Font Değiştirme - 2
Sınıf dışında
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
# QFont için
from PyQt5.QtGui import *

#Font sınıfından font nesnesi oluşturuyoruz
font = QFont()
font.setFamily('Arial')
font.setPointSize(30)
font.setBold(True)
font.setItalic(True)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Varsayımda label boş olduğunda
        # sol üst köşeye yani 0,0 konumlandırır
        self.label = QLabel('LABEL', self)
        self.label.setText('yeni label')
        self.label.move(100,100)
        # font nesnesini label'ın fontunu set etmekte kullanıyoruz.
        self.label.setFont(font)


        self.resize(800, 640)
        self.setWindowTitle("PyQt5 Label")
        self.show()


app=QApplication([])
window = Window()
app.exec()