'''
---------------------------------------------------------tw:@tek_elo
Pencereye Label Yer Değiştirme - 2
label fonksiyonu
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
        text.setText('Yeni LABEL')
        text.move(300,200)



app=QApplication([])
window = Window()
app.exec()