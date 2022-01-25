'''
---------------------------------------------------------tw:@tek_elo
Dışardan gizlediğimiz veriyi set metodu kullanarak değiştiriyoruz
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

    #Gizlediğimiz TCNo için set metodu tanımlıyoruz
    def set__TCNo(self,TcNoDuzelt):
        self.__TCNo=TcNoDuzelt

# Kimlik nosunu yanlış girdiğimiz bir öğrenci oluşturuyoruz
kaanEmre=Ogrenciler('Kaan Emre', 33, 23142343655)
print('Öğrenci TC No son 4 hane: ', kaanEmre.get_TCNo())

# Öğrencinin kimlik numarasını düzeltebilir ve tekrar yazdırabilirsiniz.
kaanEmre.set__TCNo(12309768687)
print ('Öğrenci TC No son 4 hane: ', kaanEmre.get_TCNo())