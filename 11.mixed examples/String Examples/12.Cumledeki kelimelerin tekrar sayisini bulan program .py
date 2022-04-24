print('----------------------------------------------------------tw:@tek_elo')
print('''
      Cumledeki kelimelerin tekrar sayisini bulan program
      ''')
print('---------------------------------------------------------------------\n')

def kelimeTekrarSayisi(str):
    kelimeVeFrekansi = {}
    kelimeler = str.split()

    for kelime in kelimeler:
        if kelime in kelimeVeFrekansi:
            kelimeVeFrekansi[kelime] += 1
        else:
            kelimeVeFrekansi[kelime] = 1

    return kelimeVeFrekansi

metin = ''' 
    Sizin dala konmus, hallu, bellu, gabellu, kabak bas bel baykusu,
    Bizim dala konmus, hallu, bellu, gabellu,kabak bas bel baykusuna,
    “Sen nasil bir hallu, bellu, gabellu, kabak bas bel baykususun”, demis.
    Bizim dala konmus, hallu, bellu, gabellu, kabak bas bel baykusu da,
    Sizin dala konmus, hallu, bellu, gabellu, kabak bas bel baykusuna,
'''
print(kelimeTekrarSayisi(metin))





