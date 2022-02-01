'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label Font Değiştirme - 1
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import *
# QFont için
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Varsayımda label boş olduğunda
        # sol üst köşeye yani 0,0 konumlandırır
        self.label = QLabel('LABEL', self)
        self.label.setText('yeni label')
        self.label.move(100,100)
        # str: Font, 18: Font boyutu, 100:Font kalınlığı, True: italic (varsayında false)
        self.setFont(QFont('Verdana', 18, 100, True ))

        self.resize(800, 640)
        self.setWindowTitle("PyQt5 Label")
        self.show()


app=QApplication([])
window = Window()
app.exec()