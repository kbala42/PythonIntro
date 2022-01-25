'''
---------------------------------------------------------tw:@tek_elo
__init__ metodu self dışında aldığı parametrelerde varsayım
değerler alabilir.
Eğer sınıf tanımında parametrelerden bir kısmı yada hiçbiri girilmemişse
varsayım parametreler geçerlidir
--------------------------------------------------------------------
'''
class Sinif:
    #init parametre olan değerlerin mutlaka sınıf örneği alınırken eklenmesi gerekir
    def __init__ (self,isim='Kalem', girisTarihi = 2019, demirBasNo='BA100'):
        print("Araç:",isim, girisTarihi, demirBasNo)

nesneBir = Sinif()
nesneIki = Sinif('Akıllı Tahta')
nesneUc = Sinif('Askılık',2020)
nesneDort = Sinif('Laptop',2021,'BA104')


