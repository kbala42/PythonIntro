'''
---------------------------------------------------------tw:@tek_elo
reduce ve lambda fonksiyonu carpma ve toplama
--------------------------------------------------------------------
'''
from functools import reduce
toplam=reduce(lambda x,y:x+y,[1,2,3,4])
carpim=reduce(lambda x,y:x*y,[1,2,3,4])
print(toplam)
print(carpim)
