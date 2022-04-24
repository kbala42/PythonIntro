'''
---------------------------------------------------------tw:@tek_elo
replace fonksiyonu metnin içerisinde geçen apametre içeriği ile
yeni içeriği değiştirir.
--------------------------------------------------------------------
'''
a="merhaba python"
# metin içersinde geçen p yerine P yerleştirip, yeni değişkende saklıyoruz
b=a.replace("p","P")
print(a)
print(b)
print("-----------------------------")
#Boşluk yerine alt çizgi yerleştiriyoruz
print(a.replace(" ","_"))
print("-----------------------------")
#merhaba yerine Günaydın yazdırıyoruz
print(a.replace("merhaba","Günaydın"))
