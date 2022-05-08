"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizeyi, ilk ve son karakterlerin değiştirildiği yeni bir dizeyle değiştirin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def kelimeDegistir(kelime):
    return kelime[-1] + kelime[1:-1] + kelime[0]

print(kelimeDegistir('abcd'))
print(kelimeDegistir('12345'))

