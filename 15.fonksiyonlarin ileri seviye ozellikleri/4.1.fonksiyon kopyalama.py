'''
---------------------------------------------------------tw:@tek_elo
fonksiyonlar kopyalanabilir, silinebilir
--------------------------------------------------------------------
'''
def ogrenci(*args,**kwargs):
    print("Notlar:")
    for i in args:
        print(i)
    print("------------")
    for i,j in kwargs.items():
        print(i,":",j)

ogrenci(50,90,80,ad="Hasan",soyad="Kara",sinif="10-Elk", numara=535)

sinif10B = ogrenci #ogrenci'nin bir kopyasını üretiyoruz

print("-------------------------------------------")
print()
del ogrenci # ogrenciyi siliyoruz

# Kopya fonksiyonla işlem yapabiliyoruz
sinif10B(50,100,90,ad="Halit",soyad="Ankaralı",sinif="10-Elk", numara=350)

# ogrenci fonksiyonunu sildiğimiziçin işlem yapamıyoruz
#ogrenci(20,60,60,ad="Mustafa",soyad="Tosun",sinif="10-Elk", numara=350)