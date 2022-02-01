'''
---------------------------------------------------------tw:@tek_elo
QHBoxLayout de frame and splitter kullanmak
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

        self.qsplitter()
        self.show()

    def qsplitter(self):

        hbox=QHBoxLayout(self)

        topLeft = QFrame(self)
        topLeft.setFrameShape(QFrame.StyledPanel)

        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1=QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)

        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)


app = QApplication([])
window = Window()
app.exec_()