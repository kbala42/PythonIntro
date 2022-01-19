print('----------------------------------------------------------tw:@tek_elo')
print('Verilen sayılar içinde tek sayıların toplamını bulan fonksiyon\n'
      '2. yöntem')
print('---------------------------------------------------------------------')
print()

def TekSayilariTopla(sayilar):
    sayilarinToplami=0
    for i in sayilar:
        s=int(i)
        if s%2!=0:
            sayilarinToplami+=s
    return sayilarinToplami

liste=[1, 2, 3, 4, 5, 6, 7, 9, 11, 1773, 1679]

print(TekSayilariTopla(liste))