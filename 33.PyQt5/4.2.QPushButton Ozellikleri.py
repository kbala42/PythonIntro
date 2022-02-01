'''
---------------------------------------------------------tw:@tek_elo
Pencereye QPushButton Özellikleri
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

        self.button()
        self.show()

    def button(self):
        button = QPushButton("Merhaba",self)
        #Butonuna ipucu verme
        button.setToolTip("PyQt5 butonu")
        button.resize(200,160)
        #Buton konum ayarlama
        button.move(50,50)
        # butonu disable etmek
        #button.setDisabled(True)
        # butonu enable etmek
        #button.setEnabled(True)
        # Buton fontunu ayarlama
        button.setFont(QFont('Verdana', 16))
        #İkon ekleme
        button.setIcon(QIcon('buton.png'))
        # İkon boyutunu ayarlama
        button.setIconSize(QSize(60,60))
        #imleç değiştirmek. El ile
        button.setCursor(Qt.PointingHandCursor)
        #encereyi kapatma olayı ekleme
        #button.clicked.connect(self.close)






app=QApplication([])
window = Window()
app.exec()