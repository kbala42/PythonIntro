'''
---------------------------------------------------------tw:@tek_elo
metot içinde hesaplama yaptıktan sonra dönüş değeri döndürülebilir
--------------------------------------------------------------------
'''
class Kare:
    # varsayım parametreleri tanımlıyoruz
    kenar=5
    alan=2
    def alanHesapla(self):
        self.alan=self.kenar*self.kenar
        # hesaplanan alanı geri döndürüyoruz
        return self.alan
# kare nesnesi oluşturuyoruz
kare=Kare()

#varsayım parametreleri ile alan hesaplatıyoruz
a=kare.alanHesapla()
print("Alan: ",a)

#kenar özelliğini 8 olarak değiştiriyoruz
kare.kenar=8
# alanı tekrar hesaplatıyoruz
a=kare.alanHesapla()
print("Alan: ",a)


