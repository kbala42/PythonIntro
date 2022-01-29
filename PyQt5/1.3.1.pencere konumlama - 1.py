'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresini konumlama - 1
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QWidget,QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Başlangıç konumunu belirliyoruz
        # move(x,y): ekranın sol üst köşesine göre konumlanır
        # x:sol üst köşeye göre apsis, y:sol üst köşeye göre ordinat
        self.move(150,150)
        self.resize(800,600)

app = QApplication([])
window = Window()
window.show()
app.exec()