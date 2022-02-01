'''
---------------------------------------------------------tw:@tek_elo
Pencereye QPushButton ekleme
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 640)
        self.setWindowTitle("PyQt5 QPushButton")

        self.button = QPushButton('Click',self)
        # Konumlandırma
        self.button.move(200,200)
        #Boyutunu ayarlama
        self.button.resize(120,100)



        self.show()


app=QApplication([])
window = Window()
app.exec()