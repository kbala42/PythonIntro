'''
---------------------------------------------------------tw:@tek_elo
sınıf içinde ki sınıf parametresi parametre olarak gelen değişikliği
referans lamaktadır. Sonra ki değişiklik sınıf parametresini
değiştirmediğinden çıkıştan nesne tanımını esas alıyoruz
--------------------------------------------------------------------
'''
class Personel:
    def __init__(self, age):
        #sınıf parametresi tanımı nesne parametresine göredir
        self.age = age
        #sonraki değişiklik yalnızca init fonksiyonunda kalmaktadır
        age = 15
        
    def getAge(self):
        return self.age #nesne tanımına göre

personel1 = Personel(22)

print(personel1.getAge())
