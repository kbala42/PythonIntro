'''
-------------------------------------------------------------------tw:@tek_elo

Bir stringin ilk 2 ve son 2 karakterini alma

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
'''

'''
1. çözüm
'''
metin ='Python'

if len(metin) < 2:
    print('Kelime iki harften daha az')
else:
    print(metin[0:2])
    print(metin[-2:])
print()

'''
2. çözüm
'''
metin ='Python'

def kelimeIlkVeSon(kelime):
  if len(kelime) < 2:
    return ''

  return kelime[0:2], kelime[-2:]

print(kelimeIlkVeSon(metin)[0])
print(kelimeIlkVeSon(metin)[1])

