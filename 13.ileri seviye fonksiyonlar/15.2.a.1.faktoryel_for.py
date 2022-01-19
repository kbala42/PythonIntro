# faktörlyel hesaplama
n= int(input("Faktöryelini almak istediğiniz sayıyıyı giriniz:"))
faktoryel=1
if n>0:
    for i in range(1,n+1):
        faktoryel*=i
print(faktoryel)
