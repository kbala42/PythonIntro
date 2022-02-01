'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresi açma
QtWidgets kalıtarak
--------------------------------------------------------------------
'''
# QWidgets import ediyoruz
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    # başlangıç fobksiyonunu yine kalıttığımız QtWidget
    # init fonksiyonunu devralıyoruz
    def __init__(self):
        super().__init__()

#uygulamamızı oluşturuyoruz. Parametre olarak boş bir liste veriyoruz
app = QtWidgets.QApplication([])

# Window sınıfımızdan window nesnemizi oluşturuyoruz
window = Window()

# penceremizi göstermek için show metodunu kullanıyoruz
window.show()

# sürekli göstermek için exec() metodunu kullanıyoruz
app.exec()