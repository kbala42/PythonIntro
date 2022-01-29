'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresini boyutlandırma
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QWidget,QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        #Boyutlandırmadan önceki varsayım penceresinin boyutunu yazdırıyoruz
        print(self.size())
        # penceremizi boyutlandırmayı sağlıyoruz
        self.resize(800,600)
        # Boyutlandırdan sonraki penceresinin boyutunu yazdırıyoruz
        print(self.size())


app = QApplication([])
window = Window()
window.show()
app.exec()