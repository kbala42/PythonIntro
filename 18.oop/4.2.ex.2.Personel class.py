'''
---------------------------------------------------------tw:@tek_elo
Personel sınıfı
--------------------------------------------------------------------
'''
class Personel:
    # Personel sınıfımızı tanımlıyoruz
    def __init__(self, isim, soyisim, id, maas, diller):
        # Nesne parametrelerini sınıf içi parametrelerine atıyoruz
        self.isim=isim
        self.soyisim=soyisim
        self.id=id
        self.maas=maas
        self.diller=diller
    
    # Goster metodunu tanımlıyoruz
    def Goster(self):
        print("""
            isim: {}
            soyisim: {}
            id: {}
            maas: {}
            diller: {}
        """.format(self.isim,self.soyisim,self.id,self.maas,self.diller))

    # ZamYap fonksiyonunu tanımlıyoruz
    # zamMiktari sınıftan bağımsız parametre ancak nesneye, sınıf içi değişkenle etki ediyor
    def ZamYap(self,zamMiktari):
        print("Zam yapılıyor")
        self.maas += zamMiktari

    # DilEkle metodunu tanımlıyoruz diller listesi ekleniyor
    #burada aynı şekilde nesneye
    def DilEkle(self,dil):
        self.diller.append(dil)

# personel1 nesnesini parametrelerle oluşturuyoruz
personel1=Personel("Aslan", "Demir", 122, 1000,["ingilizce","Arapça"])

# personel1 nesnesinin içeriğini gösteriyoruz
personel1.Goster()

# ZamYap fonksiyonunu çağırıyoruz
personel1.ZamYap(300)
# personel1 nesnesinin içeriğini gösteriyoruz
personel1.Goster()

# DilEkle fonksiyonunu çağırıyoruz
personel1.DilEkle("Almanca")
# personel1 nesnesinin içeriğini gösteriyoruz
personel1.Goster()