'''
---------------------------------------------------------tw:@tek_elo
reduce fonksiyonu verilen listenin bütün elmenlarına
tanımlanan fonksiyonu uygular.
--------------------------------------------------------------------
'''
from functools import reduce
# topla fonksiyonu tanımlıyoruz
def topla(x,y):
    print(f'(x={x} , y={y}) -> x  + y = {x + y}')
    return x+y

girisListesi = [1,2,3,4,5]

sonuc = reduce(topla, girisListesi)

print(type(sonuc))

print(sonuc)



