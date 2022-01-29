'''
---------------------------------------------------------tw:@tek_elo
Pencerenin başlık ve ikonlarını değiştirebiliriz
--------------------------------------------------------------------
'''
from PyQt5 import QtWidgets,QtGui
import sys

app = QtWidgets.QApplication(sys.argv)

windows = QtWidgets.QWidget()
windows.resize(500,500)
windows.move(100,100)

#Pencere başlığını belirliyoruz
windows.setWindowTitle('Merhaba')

#Pencere ikonunu belirliyoruz
windows.setWindowIcon(QtGui.QIcon('icon.png'))

windows.show()
sys.exit(app.exec_())