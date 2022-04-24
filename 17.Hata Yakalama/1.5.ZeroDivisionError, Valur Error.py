'''
---------------------------------------------------------tw:@tek_elo
Hata tutucular virgülle birleştirilerek tek hata bloğunda birleştirilebilir
--------------------------------------------------------------------
'''
try:
    sayiBir = int(input("Birinci Sayı :"))
    sayiIki = int(input("İkinci Sayı :"))
    sonuc = sayiBir/sayiIki
    print("Sonuç :",sonuc)
except (ValueError,ZeroDivisionError):
    print ("ValueError veya ZeroDivisionError hatası")
except:
    print("Beklenmeyen bir hata oluştu")