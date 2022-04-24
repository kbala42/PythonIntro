'''
---------------------------------------------------------tw:@tek_elo
Hata kaynağının nedenini göstermek için as anahtar sözcüğü kullanılır
--------------------------------------------------------------------
'''
try:
    sayi = int(input("Birinci Sayı :"))
    sonuc = sayi**2
    print("Sonuc :",sonuc)
except ValueError as hata:
    print('Lütfen sayı giriniz')
    print(hata)