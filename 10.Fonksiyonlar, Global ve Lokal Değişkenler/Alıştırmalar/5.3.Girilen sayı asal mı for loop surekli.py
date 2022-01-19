print('----------------------------------------------------------tw:@tek_elo')
print('Girilen sayı asal mı olduğunu for döngüsü ile bulan fonksiyon\n'
      'Sürekli döngü ile')
print('---------------------------------------------------------------------')
print()

def asalMi(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi):
            if(sayi % i ==0):
                return False
        return True

while True:
    sayi = input("Sayi giriniz:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

    if (asalMi(sayi)):
        print(f"{sayi} sayısı asal bir sayıdır")
    else:
        print(f"{sayi} sayısı asal bir sayı değildir")