'''
---------------------------------------------------------tw:@tek_elo
reduce fonksiyonu verilen listenin bütün elmenlarına
tanımlanan carpma fonksiyonu uygular.
--------------------------------------------------------------------
'''
from functools import reduce
# carp fonksiyonu tanımlıyoruz
def carp(x,y):
    print(f'(x={x} , y={y}) -> x * y = {x * y}')
    return x*y

girisListesi = [1,2,3,4,5]

sonuc = reduce(carp, girisListesi)

print(type(sonuc))

print(sonuc)



