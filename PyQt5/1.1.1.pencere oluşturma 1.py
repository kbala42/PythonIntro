'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresi açma
PyQt5 pencere açmak için twmwl sınıf QtWidgets'tır. BU sınıfı import edip
diğer kullanacağımız pencereleri ondan kalıtacağız
QApplicationuygulama işleyicisini ve QWidgettemel bir boş GUI
--------------------------------------------------------------------
'''
# QWidget import ediyoruz
from PyQt5.QtWidgets import *
# import'ta kullanacağımız yalnızca QWidget ve QApplication modülleri olduğundan
#from PyQt5.QtWidgets import QWidget,QApplication
# şeklinde tanımlamada hata vermeden kullanılabilir
# QApplication uygulama işleyicisini ve QWidgettemel bir boş GUI içerir

# Kodumuzda kullanmak için QtWidget'dan kalıttığımız
# Window adında bir sınıf oluşturuyoruz
class Window(QWidget):
    # başlangıç fobksiyonunu yine kalıttığımız QtWidget
    # init fonksiyonunu devralıyoruz
    def __init__(self):
        super().__init__()

#uygulamamızı oluşturuyoruz. Parametre olarak boş bir liste veriyoruz
app = QApplication([])

# Window sınıfımızdan window nesnemizi oluşturuyoruz
window = Window()

# penceremizi göstermek için show metodunu kullanıyoruz
window.show()

# sürekli göstermek için exec() metodunu kullanıyoruz
app.exec()