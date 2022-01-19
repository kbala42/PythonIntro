# faktörlyel hesaplama
def FaktoryelHesapla(n):
    faktoryel = 1
    if n == 1:
        return 1
    else:
        return n*FaktoryelHesapla(n-1)
n= int(input("Faktöryelini almak istediğiniz sayıyıyı giriniz:"))
print(FaktoryelHesapla(n))
