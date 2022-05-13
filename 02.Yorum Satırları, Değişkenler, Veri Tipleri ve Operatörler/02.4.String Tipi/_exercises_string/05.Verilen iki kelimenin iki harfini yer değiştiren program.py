"""
-------------------------------------------------------------------tw:@tek_elo
Verilen iki kelimenin iki harfini yer değiştiren program
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
'''
    1. çözüm
'''
kelime1 = 'Python'
kelime2 = 'Csharp'

yeniKelime1 = kelime2[:2] + kelime1[2:]
yeniKelime2 = kelime1[:2] + kelime2[2:]

print(yeniKelime1)
print(yeniKelime2)
print()

'''
    2. çözüm
'''
def kelimeKaristir(klm1, klm2):
  yeniKlm1 = klm2[:2] + klm1[2:]
  yeniKlm2 = klm1[:2] + klm2[2:]

  return yeniKlm1, yeniKlm2
  #return yeniKlm1 + ' ' + yeniKlm2

print(kelimeKaristir(kelime1, kelime2)[0])
print(kelimeKaristir(kelime1, kelime2)[1])
#print(kelimeKaristir(kelime1, kelime2))