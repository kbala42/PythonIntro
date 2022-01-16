print('''
-----------------------------------------------------------------------------tw:@tek_elo
Girilenbir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayinın kendi hariç bölenlerinin toplamı kendine eşitse bu sayiya "mükemmel sayi" denir.

Örnek olarak, 6 mükemmel bir sayidır. (1 + 2 + 3 = 6)
----------------------------------------------------------------------------------------''')

sayi = int(input("sayi:"))

i = 1
toplam = 0
while (i < sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1

if (toplam == sayi):
    print(sayi,"mükemmel bir sayidır.")
else:
    print(sayi,"mükemmel bir sayi değildir.")