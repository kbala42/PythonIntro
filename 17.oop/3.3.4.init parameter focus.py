'''
---------------------------------------------------------tw:@tek_elo
sınıf örneği alınırken girilen parametre fonksiyon içinde
değişikliğe uğramışsa son değişikliği referans alır
--------------------------------------------------------------------
'''
class Personel:
    def __init__(self, age):
        # age nesne tanılanırken farklı giriş alsada
        age = 15 # burada yeniden tanımlanıyor
        self.age = age # son değişiklik referans alınmaktadır

    def getAge(self):
        return self.age # dönüş son değişikliği referans lamaktadır

personel1 = Personel(22)

#Çıkışta sınıf içinde ki son tanım referans alınmaktadır.
print(personel1.getAge())
