'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label Text Değiştirme - 1
window içinde
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Varsayımda label boş olduğunda
        # sol üst köşeye yani 0,0 konumlandırır
        self.label = QLabel('LABEL', self)
        self.label.setText('yeni label')

        self.resize(800, 640)
        self.setWindowTitle("PyQt5 Label")
        self.show()


app=QApplication([])
window = Window()
app.exec()