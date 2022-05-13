"""
-------------------------------------------------------------------tw:@tek_elo

Verilen bir dizgenin sonuna 'ler' ekleyecek bir Python programı yazın
(uzunluk en az 3 olmalıdır). Verilen dize zaten 'ler' ile bitiyorsa, bunun yerine
'le' ekleyin. Belirtilen dizenin dize uzunluğu 3'ten azsa, değiştirmeden bırakın.

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def kelimeEkle(kelime):
  uzunluk = len(kelime)

  if uzunluk > 2:
    if kelime[-3:] == 'ler':
      kelime += 'le'
    else:
      kelime += 'ler'

  return kelime
print(kelimeEkle('ek'))
print(kelimeEkle('Ali'))
print(kelimeEkle('Veliler'))


