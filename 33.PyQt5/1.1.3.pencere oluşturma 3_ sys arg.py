'''
---------------------------------------------------------tw:@tek_elo
En basit PyQt5 penceresi açma - 3
Komut satırı parametrelerini uygulamada uygulayarak
--------------------------------------------------------------------
'''
from PyQt5.QtWidgets import QApplication, QWidget

# Komut satırı parametrelerine ulaşmak için sys import ediyoruz
import sys

# Uygulamamızda komut satırı parametrelerini kullanmak için
# app nesnemizi oluştururken QApplication sınıfına argüman olarak sys.argv veriyoruz
app = QApplication(sys.argv)

# Penceremizi QWidget'tan oluşturuyoruz
window = QWidget()

# Pencereler varsayımda gizli olduğu için show metodu ile gösterilmesini sağlıyoruz
window.show()

# olay döngüsünü başlatıyoruz
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.