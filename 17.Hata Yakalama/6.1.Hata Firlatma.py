'''
---------------------------------------------------------tw:@tek_elo
 raise kod içinde bir hata oluştuğunda hata fırlatmak için kullanabiliriz
 hata oluştuğunda hata mesajıda yazdırabiliriz
--------------------------------------------------------------------
'''
def tersCevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen string bir değer giriniz.")
    else:
        return s[::-1]

print(tersCevir("Merhaba"))
#print(tersCevir(456)) # sayısal bir değer girilmişse hata oluşur
        