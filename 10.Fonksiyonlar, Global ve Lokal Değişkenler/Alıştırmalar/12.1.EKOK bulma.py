print('----------------------------------------------------------tw:@tek_elo')
print('Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını\n'
      '(EKOK) dönen bir tane fonksiyon yazın.')
print('---------------------------------------------------------------------')
print()

def ekokBulma(sayiBir, sayiIki):
    i = 2
    ekok = 1
    while True:
        if (sayiBir % i == 0 and sayiIki % i == 0):
            ekok *= i

            sayiBir //= i
            sayiIki //= i


        elif (sayiBir % i == 0 and sayiIki % i != 0):
            ekok *= i

            sayiBir //= i


        elif (sayiBir % i != 0 and sayiIki % i == 0):
            ekok *= i

            sayiIki //= i
        else:
            i += 1
        if (sayiBir == 1 and sayiIki == 1):
            break
    return ekok


sayiBir = int(input("Sayı-1:"))
sayiIki = int(input("Sayı-2:"))

print("Ekok:", ekokBulma(sayiBir, sayiIki))

