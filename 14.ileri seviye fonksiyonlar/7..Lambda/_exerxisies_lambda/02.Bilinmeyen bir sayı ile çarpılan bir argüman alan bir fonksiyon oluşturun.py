"""
-------------------------------------------------------------------tw:@tek_elo
Bilinmeyen bir sayı ile çarpılan bir argüman alan bir fonksiyon oluşturun
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def hesapla(n):
 return lambda x : x * n
result = hesapla(2)
print("15 sayısının iki katı =", result(15))
result = hesapla(3)
print("15 sayısının üç katı =", result(15))
result = hesapla(4)
print("15 sayısının dört katı =", result(15))
result = hesapla(5)
print("15 sayısının beş katı =", result(15))

