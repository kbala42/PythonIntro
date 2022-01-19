print('----------------------------------------------------------tw:@tek_elo')
print('Girilen sayının çift mi tek mi olduğunu bulan fonksiyon')
print('---------------------------------------------------------------------')
print()

def SayiCiftMi (sayi):
    if sayi%2==0:
        print('Sayı çifttir')
    else:
        print('Sayı	tektir')

sayi=int(input('Bir sayı giriniz:'))
SayiCiftMi(sayi)
