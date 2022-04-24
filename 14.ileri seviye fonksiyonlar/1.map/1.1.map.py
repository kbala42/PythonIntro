'''
---------------------------------------------------------tw:@tek_elo
map fonksiyonu ygulandığı verilerin herbirine
girilen fonksiyonu yürütür
--------------------------------------------------------------------
'''
# kare alma fonksiyonu tanımlıyoruz
def kareAl(x):
    return x**2

k = map(kareAl,[1,2,3,4,5])

print(type(k))

print(k)

print(list(k))