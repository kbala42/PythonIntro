'''
---------------------------------------------------------tw:@tek_elo
QCalendarWidget Ekleme
--------------------------------------------------------------------
'''
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.calendar()
        self.show()

    def calendar(self):

        self.calendar = QCalendarWidget(self)
        self.calendar.move(20,20)
        self.calendar.setGridVisible(True)

        self.calendar.clicked.connect(self.printDataInfo)

    def printDataInfo(selfself,qDate):
        print("{}/{}/{}".format(qDate.day(),qDate.month(),qDate.year()))


app = QApplication([])
window = Window()
app.exec_()