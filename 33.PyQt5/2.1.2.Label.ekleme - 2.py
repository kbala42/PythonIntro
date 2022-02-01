'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label ekleme - 2
Ayrı bir label fonksiyonu çağırarak
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label()

        self.setWindowTitle("PyQt5 Label")
        self.resize(800, 640)
        self.show()

    def label(self):
        #label'ın text kısmında gözükecek text
        text=QLabel("Merhaba",self)



app=QApplication([])
window = Window()
app.exec()