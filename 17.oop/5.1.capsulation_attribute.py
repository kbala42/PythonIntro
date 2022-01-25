'''
---------------------------------------------------------tw:@tek_elo
Veri kapsülleme tek birim altında nitelikleri ve metotları gruplamayı
tanımlar. Böylece nitelikleri dışardan gizleyebiliriz
--------------------------------------------------------------------
'''
# self.__TCNo=TCNo kullanımı öğrencinin kimlik numarasına dışarıdan erişimi engeller.
class Ogrenciler:
    def __init__(self,adi,yasi,TCNo):
        self.adi=adi
        self.yasi=yasi
        # self.__TCNo kullanarak kimlik numarasını dışardan gizliyoruz, erişimi engelliyoruz
        self.__TCNo=TCNo

    def ogrenciYaz(self):
        print('Öğrenci Bilgileri')
        print(self.adi)
        print(self.yasi)
        print(self.__TCNo) #sınıf parametresini doğrudan kullandığımızda fonksiyondan erişebiliriz

muratCaliskan=Ogrenciler('Murat Çalışkan',17,54639876211)
muratCaliskan.ogrenciYaz()
print('---------------------------------')
# Öğrenci bilgilerine doğrudan erişmeyi deneyoruz
print (muratCaliskan.adi)
print (muratCaliskan.yasi)
# Doğrudan __TCNo erişemiyoruz. Hata alıyoruz
print (muratCaliskan.__TCNo)