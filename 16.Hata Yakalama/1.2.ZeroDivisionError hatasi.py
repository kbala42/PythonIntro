'''
---------------------------------------------------------tw:@tek_elo
ZeroDivisionError hatası sıfıra bölme durumunda meydana gelecek
hatayı tutmak için kullanılır
--------------------------------------------------------------------
'''
sayiBir = int(input("Birinci Sayı :"))
sayiIki = int(input("İkinci Sayı :"))
try:
    sonuc = sayiBir/sayiIki
    print("Sonuç :",sonuc)
except ZeroDivisionError:
    print ("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")