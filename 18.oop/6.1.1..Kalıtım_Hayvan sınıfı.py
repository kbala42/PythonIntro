'''
---------------------------------------------------------tw:@tek_elo
Sınıftan yeni sınıflar kalıtabilir, onlara yeni metot ve özellikler katabiliriz
--------------------------------------------------------------------
'''
# Temel sınıfımız üretiyoruz
class Hayvan():
    def __init__(self):
        print("Hayvan nesnesi üretildi")

    def turunuYazdir(self):
        print("Hayvan")

    def yurume(self):
        print("Hayvanlar genelde yürüyebilir")

# Penguen sınıfını temel Hayvan sınıfımızdan kalıtıyoruz
class Penguen(Hayvan):
    def __init__(self):
        # Hayvan sınıfının __init__ kullanabiliyoruz. Bunu da
        # super() fonksiyonu ile yapıyoruz
        super().__init__()
        print("Penguen nesnesi üretildi")

    def turunuYazdir(self):
        print("Penguen")

    def yuzme(self):
        print("Penguenler iyi yüzücüdür")

# Aslan sınıfını temel Hayvan sınıfımızdan kalıtıyoruz
class Aslan(Hayvan):
    def __init__(self):
        # Hayvan sınıfının __init__ kullanabiliyoruz. Bunu da
        # super() fonksiyonu ile yapıyoruz
        super().__init__() #Hayvan sınıfının __init__ kullanabiliyoruz
        print("Aslan nesnesi üretildi")

    def turunuYazdir(self):
        print("Aslan")

    def kukreme(self):
        print("Aslan kükrer")

hayvan=Hayvan()
hayvan.turunuYazdir()
hayvan.yurume()

print("-------------------")

# pengeuen nesnesi üretilirken Hayvan sınıfına ait
# __init__ fonksiyonu da devreye girmektedir
penguen=Penguen()
penguen.turunuYazdir()
penguen.yuzme()

print("-------------------")

# aslan nesnesi üretilirken Hayvan sınıfına ait
# __init__ fonksiyonu da devreye girmektedir
aslan=Aslan()
aslan.turunuYazdir()
aslan.kukreme()