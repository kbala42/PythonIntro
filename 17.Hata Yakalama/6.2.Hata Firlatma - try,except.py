'''
---------------------------------------------------------tw:@tek_elo
 try-except kod bloğu içinde raise hata fırlatıcı  kullanılarak
 hata verdirmeden çalıştırılabilir
--------------------------------------------------------------------
'''
def tersCevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen string bir değer giriniz.")
    else:
        return s[::-1]

try:
    print(tersCevir(456))
except:
    print("Fonksiyon hata verdi")

        