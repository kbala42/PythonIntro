'''
---------------------------------------------------------tw:@tek_elo
QFormLayout Özellikler
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

        #form üretiyoruz
        self.form = QFormLayout(self)

        self.form.addWidget(QLabel('Kullanıcı Girişi'))
        self.form.addRow(QLabel('Kullanıcı Adı: '), QLineEdit())
        self.form.addRow(QLabel('Kullanıcı Şifresi: '), QLineEdit())
        self.form.addRow(QPushButton('Tamam'),QPushButton('Vazgeç'))

        #Varsayım otomatik boyutlandırma
        #self.form.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)

        # Hizalama
        #self.form.setFormAlignment(Qt.AlignCenter)

        self.show()


app = QApplication([])
window = Window()
app.exec_()