from functools import reduce

def maksimum(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(maksimum,[5,1,8,3,4]))
