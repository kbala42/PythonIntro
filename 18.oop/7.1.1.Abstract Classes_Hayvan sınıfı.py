'''
---------------------------------------------------------tw:@tek_elo
Soyut temel sınıflar üretmek için Python'da abc modülünü kullanıyoruz.
Bunun içinde abc modülünden ABC ve abstractmethod dahil etmeliyiz
--------------------------------------------------------------------
'''
from abc import ABC, abstractmethod

# ABC sınıfından Hayvan soyut sınıfını üretiyoruz
class Hayvan(ABC):

    #soyut metot için abstractmethod geniişletme yapıyoruz
    @abstractmethod
    def turunuYazdir(self):pass

    # soyut metot için abstractmethod geniişletme yapıyoruz
    @abstractmethod
    def yurume(self):pass

print(Hayvan)
print(type(Hayvan))

