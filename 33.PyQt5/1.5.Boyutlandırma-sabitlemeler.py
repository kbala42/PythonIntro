'''
---------------------------------------------------------tw:@tek_elo
Pencere gösterme özellikleri, pencerenin başlangıçtaki durumunu yada
bir olay sonunda (buton tıklama) durumunu belirler
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        # Pencerenin gösterilmesi için kullanılan metot
        self.show()
        # Pencerenin minimum gösterilmesi için kullanılan metot.
        # Başlatma çubuğunda ikon olarak gösterir
        # self.showMinimized()
        # Pencerenin maksimum gösterilmesi için kullanılan metot.
        #self.showMaximized()
        # Pencerenin tam ekran gösterilmesi için kullanılan metot.
        #self.showFullScreen()
        # Pencerenin normal boyutta gösterilmesi için kullanılan metot.
        #self.showNormal()


window = Window()
sys.exit(app.exec_()) # ana döngüyü yürütmek için