'''
---------------------------------------------------------tw:@tek_elo
1000'e kadar olan sayilardan asal sayiları üreten generator fonksiyonu
-------------------------------------------------------------------
'''
def asalMi(sayi):
    i = 2
    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True

def asalGenerator():
    i = 2
    while True:
        if (asalMi(i)):
            yield i
        i += 1


for sayi in asalGenerator():
    if (sayi > 1000):
        break
    print(sayi)