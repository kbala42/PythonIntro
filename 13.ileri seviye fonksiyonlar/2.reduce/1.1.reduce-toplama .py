from functools import reduce

def topla(x,y):
    return x+y

sonuc=reduce(topla,[1,2,3,4,5])

print(type(sonuc))
print(sonuc)
