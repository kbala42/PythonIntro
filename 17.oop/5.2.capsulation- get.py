'''
---------------------------------------------------------tw:@tek_elo
Sınıf içinde ki gizlenmiş parametreleri okumak için get özelliğini kullanıyoruz
--------------------------------------------------------------------
'''
class Ogrenciler:

    def __init__(self,adi,yasi,TCNo):
        self.adi=adi
        self.yasi=yasi
        self.__TCNo=TCNo

    def ogrenciYaz(self):
        print('Öğrenci Bilgileri')
        print(self.adi)
        print(self.yasi)
        print(self.__TCNo)

    def get_TCNo(self):
        #tanımladığımız get metodumuzda 7. ve sonrası karakterleri alıyoruz
        return str(self.__TCNo) [7:]

ogrenci=Ogrenciler('Sezai', 43, 12345678901)
print('....',ogrenci.get_TCNo())