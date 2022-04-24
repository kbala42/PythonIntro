'''
---------------------------------------------------------tw:@tek_elo
Eğer soyut sınıfta ki metotlarda
abstractmethod tanımlanmamışsa kalıtılan sınıfta bu metodu tanımlamak
zorunda değiliz
--------------------------------------------------------------------
'''
from abc import ABC, abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def turunuYazdir(self):pass
    # abstractmethod tanımlanmamış
    def yurume(self):pass

class Penguen(Hayvan):

    def __init__(self):
        print("Penguen")

    # abstract method girilen metot alt sınıfta yazılmalıdır
    def turunuYazdir(self):pass

    #yurume metodu abstract girilmediğinden tanımlanmak zorunda değildir

print(Penguen)
print(type(Penguen))
penguen=Penguen()

