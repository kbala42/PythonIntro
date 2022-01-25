'''
---------------------------------------------------------tw:@tek_elo
Öğrenci sınıfı
Sınıf içi liste, tanımda olmayan öğrencşye ait özelliklerin girişleri
--------------------------------------------------------------------
'''
class Ogrenci():
    # __doc__ fonksiyonu için tanım
    '''Öğrenci Sınıfı'''
    ogrenciler=[] #ogrenci listesi tanımlıyoruz

    #Başlatma fonksiyonunu tanımlıyoruz. Burada tanımlı tek parametremzi var
    def __init__(self, ogrenciAdiSoyadi):
        #Nesne parametrelerini sınıf parametrelerine atıyoruz
        self.ogrenciAdiSoyadi = ogrenciAdiSoyadi
        self.dersleri=[] # Boş dersler listesi üretiyoruz
        self.sinavlar=[] # Boş sinavlar listesi üretiyoruz
        self.OgrenciEkle(self.ogrenciAdiSoyadi) #Öğrenci eklemesi için OgrenciEkle fonksiyonunu ekliyoruz

    # OgrenciEkle fonksiyonunu tanımlıyoruz. ogrenciler listesine ekleme yapmaktayız
    def OgrenciEkle(self, ogrenciAdiSoyadi):
        self.ogrenciler.append(ogrenciAdiSoyadi) # Oluşturduğumuz öğrenci(ogrenci)  ogrenciler listesine ekliyoruz
        print('{} adlı kişi öğrencilere eklendi'.format(ogrenciAdiSoyadi)) # Eklenen öğrenci için çıkış

    # ogrenciler listesi için yazdırma metodu
    def OgrenciListesiYazdir(self):
        print('Öğrenci Listesi')
        for ogrenci in self.ogrenciler:
            print(ogrenci)

    # dersleri listesine ekleme metodu tanımlıyoruz
    def DersEkle(self, dersAdi):
        self.dersleri.append(dersAdi)

    # öğrenciye ait dersleri yazdırma metodu
    def OgrancininDersleri(self):
        print('{} adlı kişinin dersleri'.format(self.ogranciAdiSoyadi))
        for ders in self.dersleri:
            print(ders)

    # sinavlar listesine puan ekleme metodu
    def SınavPuaniEkle(self,sinavPuani):
        self.sinavlar.append(sinavPuani)

    # sinavlar listesini yazdırma metodu
    def OgrencininSinavPuanlari(self):
        print('{] adlı kişinin sınav sonuçları:'.format(self.ogranciAdiSoyadi))
        for sinav in self.sinavlar:
            print(sinav)

# Nesne oluşturuyoruz
tosunDemir=Ogrenci('Tosun Demir')
#nesnenin hafıza adresi
print(id(tosunDemir))
# sınıfın niteliklerini listeliyoruz
print(dir(tosunDemir))
# sınıf dokümantasyonu
print(tosunDemir.__doc__)

