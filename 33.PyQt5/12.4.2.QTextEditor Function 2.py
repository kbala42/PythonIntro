'''
---------------------------------------------------------tw:@tek_elo
QFontComboBox Kullanımı
Açılır Font seçim yapmak iiçin kullanıyoruz
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

        self.textEditor()
        self.show()

    def textEditor(self):

        self.editor = QTextEdit(self)
        self.editor.move(300,200)

        button = QPushButton("Text Editor",self)
        button.move(300, 150)
        button.clicked.connect(self.texEditorFunction)

    def texEditorFunction(self):
        # Plain text'te dönüştürme
        text = self.editor.toPlainText()
        print(text)




app = QApplication([])
window = Window()
app.exec_()