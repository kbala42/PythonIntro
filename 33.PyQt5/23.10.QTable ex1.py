from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import numpy as np

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000, 640)
        self.setWindowTitle("PyQt5 Penceresi")

        self.tab()
        self.show()

    def tab(self):

        vbox = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Başlık1"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Başlık2"))

        dizi=np.array([[1,2],[3,4]])
        for r in range(dizi.shape[0]):
            for c in range(dizi.shape[1]):
                self.table.setItem(r,c,QTableWidgetItem(str(dizi[r,c])))

        button=QPushButton("Table")
        button.clicked.connect(self.getValue)

        vbox.addWidget(self.table)
        #vbox.addWidget(self.button)
        self.setLayout(vbox)

    def getValue(self):
        for item in self.table.selectedItems():
            print("row {},column {}, Değer: {}".format(item.row(),item.column(),item.value()))









window = Window()
sys.exit(app.exec_()) # mainloop