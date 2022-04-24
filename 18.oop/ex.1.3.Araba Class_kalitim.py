'''
---------------------------------------------------------tw:@tek_elo
Araba sınıfıdan kalıtım örneği
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
        print('{} model {} kapılı {} renkli {} marka araç motor seri no:{}'.format(self.model,self.kapiSayisi,self.rengi,self.marka, self.__motorSeriNo))

    def get_MotorSeriNo(self):
        return self.__motorSeriNo

    def set_motorSeriNo(self,motorSeriNoDuzeltme):
        self.__motorSeriNo=motorSeriNoDuzeltme

# Yeni sınıf kalıtıyoruz
class ArabaSinifim(Araba):
    celikJant=True
    def GazVer(self):
        print(self.marka,'Durum:Gaza basıldı')

yeniAraba=ArabaSinifim('Marka 456', 1992)
yeniAraba.GazVer()
yeniAraba.ArabaOzellikleri()