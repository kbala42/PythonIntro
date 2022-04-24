'''
---------------------------------------------------------tw:@tek_elo
Sınıflar içinde sunulan davranışlardır. Davranılar sınıf içinde
tanımlı fonksiyonlarla sağlanır
--------------------------------------------------------------------
'''
class Ogrenci:
    #attributes
    yas=15
    sinifi=9
    dogumYeri="Yalova"

    # behaviours
    def notTut(self):
        print("not tutuyor")
    def resimCiz(self):
        print("resim çiziyor")

ogrenci1=Ogrenci()
ogrenci2=Ogrenci()

# nesneye ait davranışlara nesneye aitlik bildiren nokta ile erişiyoruz
ogrenci1.notTut()
ogrenci1.resimCiz()
print("---------------------------------")
ogrenci2.notTut()
ogrenci2.resimCiz()
