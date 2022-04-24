'''
---------------------------------------------------------tw:@tek_elo
set fonksiyonu da dışarından erişilememesi ve yalnızca sınıf içinden
erişilebilmesi için private(özel) hale getirilebilir
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
        return str(self.__TCNo) [7:]

    def __set__TCNo(self,TcNoDuzelt):
        self.__TCNo=TcNoDuzelt


ogrenci=Ogrenciler('Kaan Emre', 33, 23142343655)
print('Öğrenci TC No son 4 hane: ', ogrenci.get_TCNo())

# Dışarından erişilemesi için set fonksiyonunu private hale getirdik.
ogrenci.__set__TCNo(12309768687)
