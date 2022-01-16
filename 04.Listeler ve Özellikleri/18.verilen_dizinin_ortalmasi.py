print('-------------------------------------------------------------@tek_elo')
print('Verilen listenin ortalamasını bulan program')
print('---------------------------------------------------------------------')
print()

sayilar_dizisi=[1,2,3,4,5]
toplam=0

for i in sayilar_dizisi:
    toplam+=i

ortalama= toplam/len(sayilar_dizisi)

print(ortalama)