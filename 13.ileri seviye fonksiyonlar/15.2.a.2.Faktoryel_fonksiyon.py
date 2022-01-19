# faktörlyel hesaplama
def FaktoryelHesapla(n):
    faktoryel = 1
    if n > 0:
        for i in range(1,n+1):
            faktoryel*=i
    return faktoryel
n= int(input("Faktöryelini almak istediğiniz sayıyıyı giriniz:"))
print(FaktoryelHesapla(n))
