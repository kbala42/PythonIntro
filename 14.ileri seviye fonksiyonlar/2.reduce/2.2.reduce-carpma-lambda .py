'''
---------------------------------------------------------tw:@tek_elo
reduce fonksiyonu ile lamda fonksiyonunun kullanımı : carpma
--------------------------------------------------------------------
'''
from functools import reduce

sonuc=reduce(lambda x,y:x*y,[1,2,3,4,5])
print(sonuc)
