'''
---------------------------------------------------------tw:@tek_elo
QTabWidgetÖzellikler
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

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(50,50, 900, 550)

        self.widget1 = QWidget()
        self.buton1 = QPushButton('Tıkla',self.widget1)

        self.widget2 = QWidget()
        self.label2 = QLabel('Seçim 2',self)

        self.widget3 = QWidget()
        self.buton3 = QPushButton('Tıkla',self.widget3)

        self.tabWidget.addTab(self.widget1, QIcon('buton.PNG'),'Sekme 1')
        self.tabWidget.addTab(self.widget2, QIcon('buton.PNG'),'Sekme 2')
        self.tabWidget.addTab(self.widget3, QIcon('buton.PNG'),'Sekme 3')

        #sekmelerin hareket etmesini sağlama
        self.tabWidget.setMovable(True)
        #sekmelerin kapatabilme özelliği
        #self.tabWidget.setTabsClosable(True)

        #varsayım sekmesini seçme 1
        self.tabWidget.setCurrentIndex(1)

        #varsayım sekmesini seçme 2
        #self.tabWidget.setCurrentWidget(self.widget3)

        #ipuçları
        self.tabWidget.setTabToolTip(0,'ipucu 1')
        self.tabWidget.setTabToolTip(1,'ipucu 2')
        self.tabWidget.setTabToolTip(2,'ipucu 3')

        #Sekmeyi etkinsizleştirme
        #self.tabWidget.setTabEnabled(0,False)

        #Sekmeyi görünmez yapma (varlığı devam ediyor)
        #self.tabWidget.setTabVisible(0,False)

        #Sekme kaldırma (Sekme tamamen siliniyor)
        #self.tabWidget.removeTab(1)

        #Sekme ekleme
        #self.tabWidget.insertTab(1, self.widget2,'Sekme 4')

        #index sayısını yazdırma
        print(self.tabWidget.count())

        #Sekmenin indeksini öğrenme
        print(self.tabWidget.indexOf(self.widget3))







        self.show()




app = QApplication([])
window = Window()
app.exec_()