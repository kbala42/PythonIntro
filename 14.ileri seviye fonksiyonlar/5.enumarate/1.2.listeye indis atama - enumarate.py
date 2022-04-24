'''
---------------------------------------------------------tw:@tek_elo
bir listeye indis atama işlemini enumarate fonksiyonu ile yapılabilir
--------------------------------------------------------------------
'''
liste = ["Konya","Yalova","Denizli","Van"]
# dönüş enumerate sınıfndan nesne
print(type(enumerate(liste)))
print(enumerate(liste))
# içeriği yazdırıyoruz
print(*enumerate(liste))
print("-------------------------")
# sonucu listeye dönüştürerek yazdırıyoruz
sonuc=list(enumerate(liste))

print(sonuc)
