'''
---------------------------------------------------------tw:@tek_elo
 Ortalama hesaplayan program
 Girişin yalnızca tam sayı girilmesi durumunda çalışır
 hatalı bir girişte hatayı yazdırır
--------------------------------------------------------------------
'''
s1 = input("ilk sayi: ")
s2 = input("ikinci sayi: ")
try:
    sayi1=int(s1)
    sayi2=int(s2)
    sonuc=(sayi1+sayi2)/2
    print(sonuc)
except ValueError as hata:
    print(hata)