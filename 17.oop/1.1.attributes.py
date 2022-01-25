'''
---------------------------------------------------------tw:@tek_elo
Nesneyi ad, boy, sınıf vb. niteleyen özellikleridir
--------------------------------------------------------------------
'''
#Ongrenci sınıfı oluşturuyoruz
class Ogrenci:
    #attributes
    yas=15
    sinifi=9
    dogumYeri="Yalova"

# Ogranci sınıfından iki nesne üretiyoruz
ogrenci1=Ogrenci()
ogrenci2=Ogrenci()

# ogrenci1 ve ogrenci2 nesneleri aynı sınıftan üretildiklerinden
# aynı özellikleri taşırlar
# nesnenin özelliğine ulaşmak için isimden sonra nokta kullanıyoruz

print("1. Öğrencinin yaşı:",ogrenci1.yas)
print("1. Öğrencinin sınıfı:",ogrenci1.sinifi)
print("1. Öğrencinin doğum yeri:",ogrenci1.dogumYeri)

print("-----------------------------")

print("2. Öğrencinin yaşı:",ogrenci2.yas)
print("2. Öğrencinin sınıfı:",ogrenci2.sinifi)
print("2. Öğrencinin doğum yeri:",ogrenci2.dogumYeri)
print("-----------------------------")
