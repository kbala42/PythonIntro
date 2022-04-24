'''
---------------------------------------------------------tw:@tek_elo
finally bir hata olmazsa da çalışacak kod bloğunu gösterir
--------------------------------------------------------------------
'''
try:
    sayiBir = int(input("Birinci Sayı :"))
    sayiIki = int(input("İkinci Sayı :"))
    sonuc = sayiBir/sayiIki
    print("Sonuç :",sonuc)
except ZeroDivisionError:
    print ("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")
except ValueError:
    print("Lütfen sayısal bir değer girin")
finally:
    print("Hata olsa da olmazsa da çalışacak blok ")

print("Blok sonu")