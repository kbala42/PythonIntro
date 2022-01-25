'''
---------------------------------------------------------tw:@tek_elo
Örnek: Masa lambası sınıfı
--------------------------------------------------------------------
'''
class MasaLambasi:
    #varsayım özellikleri tanımlıyoruz
    isikRengi='Sarı'
    isikDurumu=False
    def IsikAc(self):
        self.isikDurumu=True
        return 'Aydinlik'
#Sınıf adı ile ulasma
MasaLambasi.isikRengi

#masaLambası nesnesini
masaLambasi=MasaLambasi()
#ışık durumunu yazdırıyoruz
print(masaLambasi.isikDurumu)
#IsikAc metodunu çağrıyoruz ve dönen değeri yazdırıyoruz
print(masaLambasi.IsikAc())
#ışık durumunu yazdırıyoruz
print(masaLambasi.isikDurumu)