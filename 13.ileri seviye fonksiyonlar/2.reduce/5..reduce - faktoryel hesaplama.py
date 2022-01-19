from functools import reduce

n=int(input("faktöryelini alacağımız sayıyı giriniz:"))
faktoryel=reduce(lambda x,y:x*y,[i for i in range(1,n+1)])
print(faktoryel)