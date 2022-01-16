print('''
-----------------------------------------------------------------------------tw:@tek_elo
Girilen bir sayının "Armstrong" sayısı olup olmadığını bulan program

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan\n
herbirinin 4. kuvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse\n
bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
----------------------------------------------------------------------------------------''')

sayi = input("Bir sayı giriniz:")
basamak_sayisi = len(sayi)
sayi = int(input("Bir sayı giriniz:"))
basamak = 0
toplam = 0

gecici_sayi = sayi

while (gecici_sayi > 0):
    basamak = gecici_sayi % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayi //= 10

if (toplam == sayi):
    print(sayi, " bir armstrong sayısıdır.")
else:
    print(sayi, " bir armstrong sayısı değildir.")