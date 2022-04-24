'''
---------------------------------------------------------tw:@tek_elo
Belirli hata tutucuların dışında başka bir hata oluşmuşsa
yürütülen blok
--------------------------------------------------------------------
'''
try:
    sayiBir = int(input("Birinci Sayı :"))
    sayiIki = int(input("İkinci Sayı :"))
    sonuc = sayiBir/sayiIki
    print("Sonuç :",sonuc)
except ZeroDivisionError:
    print ("Bir sayıyı sıfıra bölemezsiniz. Lütfen sıfır dışında bir sayı girin")
except ValueError:
    print("Lütfen sayısal bir değer girin")
except:
    print("Beklenmeyen bir hata oluştu")