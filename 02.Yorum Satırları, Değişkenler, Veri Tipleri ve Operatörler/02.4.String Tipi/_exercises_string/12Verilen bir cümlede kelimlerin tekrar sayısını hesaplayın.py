"""
-------------------------------------------------------------------tw:@tek_elo

Verilen bir cümlede kelimlerin tekrar sayısını hesaplayan program

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def kelimeSay(mtn):
    sayilanlar = dict()
    kelimeler = mtn.split()

    for kelime in kelimeler:
        if kelime in sayilanlar:
            sayilanlar[kelime] += 1
        else:
            sayilanlar[kelime] = 1

    return sayilanlar

metin = 'the quick brown fox jumps over the lazy dog.'
print( kelimeSay(metin))

