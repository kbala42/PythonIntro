'''
---------------------------------------------------------tw:@tek_elo
reduce fonksiyonu carpma örneği
--------------------------------------------------------------------
'''
from functools import reduce

def maksimum(x,y):
    if x>y:
        print(f'(x={x} , y={y}) -> x > y = {x}')
        return x
    else:
        print(f'(x={x} , y={y}) -> x < y = {y}')
        return y

print(reduce(maksimum,[5,1,8,3,4]))

