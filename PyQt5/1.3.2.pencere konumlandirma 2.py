'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresini konumlama - 2
init fonksiyonu kullanmadan
--------------------------------------------------------------------
'''
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.move(100,100)
window.resize(500,500)

window.show()
sys.exit(app.exec_())