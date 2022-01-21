'''
---------------------------------------------------------tw:@tek_elo
reduce fonksiyonu ile lamda fonksiyonunun kullanımı : toplama
--------------------------------------------------------------------
'''
from functools import reduce

girisListesi = [1,2,3,4,5]

sonuc=reduce(lambda x,y:x+y, girisListesi)

print(sonuc)
