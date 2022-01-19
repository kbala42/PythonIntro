print('----------------------------------------------------------tw:@tek_elo')
print('Girilen iki sayının EBOB\ bulan fonksiyon')
print('---------------------------------------------------------------------')
print()

def ebobBul(sayiBir, sayiIki):
    i = 1
    ebob = 1
    while (i <= sayiBir and i <= sayiIki):

        if (not (sayiBir % i) and not (sayiIki % i)):
            ebob = i
        i += 1
    return ebob


sayiBir = int(input("Sayı-1:"))
sayiIki = int(input("Sayı-2:"))

print("Ebob:", ebobBul(sayiBir, sayiIki))