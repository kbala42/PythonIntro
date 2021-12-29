metin='Merhaba Python'
print (metin[0]) # ifadenin ilk karakterini yazar.
print (metin[4:7]) # ifadenin 5, 6 ve 7. karakterlerini yazar.
print (metin[8::]) # 9. karakterden sonuncu karaktere kadar yazar.
print (metin[-2]) # karakter dizisinin en sondan ikinci karakterini yazar.
print (metin [:]) # Bütün ifadeyi yadırır
print (metin [:7]) # indisi 0' dan 7'ye kadar olan (7 dahil değil) karakterleri yazar.
print (metin[8:]) # başlangıç indisinden sonra tüm karakterleri yazar.
print (metin [:-4]) # -4. karaktere kadar bütün ifadeyi yadırır
print(metin[::3]) # 0, 3, 6, 9 ve 12 indis numaralı karakterleri dilimler.
print(metin[:8:2]) # 0, 2, 4 ve 6 indis numaralı karakterleri dilimler.
print (metin[::-1]) # ifadeyi ters döndürme