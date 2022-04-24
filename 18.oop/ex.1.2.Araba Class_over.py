'''
---------------------------------------------------------tw:@tek_elo
Araba sınıfı örneği
get ve set fonksiyonları
--------------------------------------------------------------------
'''
class Araba:
    __doc__ = 'Araba Sınıfı'
    isikDurumu=False
    def __init__(self,marka=None, model=None, kapiSayisi=2, rengi=None, fiyati=None, motorSeriNo=None):
        self.marka=marka
        self.model=model
        self.kapiSayisi=kapiSayisi
        self.rengi = rengi
        self.fiyati=fiyati
        self.__motorSeriNo=motorSeriNo

    def ArabaOzellikleri(self):
        print('{} model {} kapılı {} renkli {} marka araç'.format(self.model,self.kapiSayisi,self.rengi,self.marka))

    def get_MotorSeriNo(self):
        return self.__motorSeriNo

    def set_motorSeriNo(self,motorSeriNoDuzeltme):
        self.__motorSeriNo=motorSeriNoDuzeltme

arabam=Araba('Marka 123', 1981)
arabam.ArabaOzellikleri()
arabam.set_motorSeriNo(123456) #Yeni serino girişi
print(arabam.get_MotorSeriNo())