'''
---------------------------------------------------------tw:@tek_elo
Araba sınıfı örneği
--------------------------------------------------------------------
'''
class Araba:
    def __init__(self,marka=None, model=None, kapiSayisi=2,rengi=None, fiyati=None, motorSeriNo=None):
        self.marka=marka
        self.model=model
        self.kapiSayisi=kapiSayisi
        self.rengi = rengi
        self.fiyati=fiyati
        self.motorSeriNo=motorSeriNo

    def ArabaOzellikleri(self):
        print('{} model {} kapılı {} renkli {} marka araç'.format(self.model,self.kapiSayisi,self.rengi,self.marka))

arabam=Araba('Marka 00', 1993,2,'sarı',motorSeriNo=123456789)
arabam.ArabaOzellikleri()