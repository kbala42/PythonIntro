'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label ekleme - 1
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Varsayımda label boş olduğunda
        # sol üst köşeye yani 0,0 konumlandırır
        self.label = QLabel('LABEL', self)

        self.resize(800, 640)
        self.setWindowTitle("PyQt5 Label")
        self.show()


app=QApplication([])
window = Window()
app.exec()