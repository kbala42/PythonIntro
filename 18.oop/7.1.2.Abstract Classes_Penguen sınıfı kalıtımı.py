'''
---------------------------------------------------------tw:@tek_elo
Soyut temel sınıftan kalıtım yapmak
--------------------------------------------------------------------
'''
from abc import ABC, abstractmethod

# Soyut sınıfımızı tanımlıyoruz
class Hayvan(ABC):
    @abstractmethod
    def turunuYazdir(self):pass

    @abstractmethod
    def yurume(self):pass

# Soyut sınıftan eni sınıf kalıtıyoruz
class Penguen(Hayvan):
    #Kalıtılan sınıftan init fonksiyonu tanımlıyoruz
    def __init__(self):
        print("Penguen")

    # abstractmethod girilen metot alt sınıfta yazılmalıdır
    def turunuYazdir(self):pass

    # abstractmethod girilen metot alt sınıfta yazılmalıdır
    def yurume(self):pass

print(Penguen)
print(type(Penguen))
penguen=Penguen()

