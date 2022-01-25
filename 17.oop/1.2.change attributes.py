'''
---------------------------------------------------------tw:@tek_elo
Nesneye ait özellikler o özelliğe ulaşılarak değiştirilebilir
--------------------------------------------------------------------
'''
class Ogrenci:
    #attributes
    yas=15
    sinifi=9
    dogumYeri="Bursa"

ogrenci1=Ogrenci()
ogrenci2=Ogrenci()

print("1. Öğrencinin yaşı:",ogrenci1.yas)
print("2. Öğrencinin yaşı:",ogrenci2.yas)

print("-----------------------------")

ogrenci1.yas=16
print("1. Öğrencinin yaşı:",ogrenci1.yas)
print("2. Öğrencinin yaşı:",ogrenci2.yas)

print("-----------------------------")

ogrenci2.yas=17
print("1. Öğrencinin yaşı:",ogrenci1.yas)
print("2. Öğrencinin yaşı:",ogrenci2.yas)

print("-----------------------------")

ogrenci1.dogumYeri="Konya"
ogrenci2.dogumYeri="Yalova"
print("1. Öğrencinin yaşı:",ogrenci1.dogumYeri)
print("2. Öğrencinin yaşı:",ogrenci2.dogumYeri)
