'''
---------------------------------------------------------tw:@tek_elo
Bir den fazla tutucu aynı anda kullanılabilir
--------------------------------------------------------------------
'''
try:
    sayiBir = int(input("Birinci Sayı :"))
    sayiIki = int(input("İkinci Sayı :"))
    sonuc = sayiBir/sayiIki
    print("Sonuç :",sonuc)
except ZeroDivisionError: # sıfıra bölme hatası tutucu
    print ("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")
except ValueError:#tam sayı dışında bir değer girilmesi durumunda oluşacak hata tutucu
    print("Lütfen sayısal bir değer girin")
