print('----------------------------------------------------------tw:@tek_elo')
print('1\'den 1000\'e kadar olan sayılardan mükemmel sayı olanları ekrana\n'
      'yazdıran fonksiyon.\n'
      'Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.\n'
      'Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).')
print('---------------------------------------------------------------------')
print()

def mukemmel(sayı):
    toplam = 0

    for i in range(1, sayı):

        if (sayı % i == 0):
            toplam += i

    return toplam == sayı


for i in range(1, 1001):
    if (mukemmel(i)):
        print("Mükemmel Sayı:", i)