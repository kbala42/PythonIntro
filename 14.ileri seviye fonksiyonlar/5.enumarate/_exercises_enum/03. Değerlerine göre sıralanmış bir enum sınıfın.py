"""
-------------------------------------------------------------------tw:@tek_elo

 Değerlerine göre sıralanmış bir enum sınıfının tüm üye adını görüntüleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
import enum
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('Country Name ordered by Country Code:')
print('\n'.join('  ' + c.name for c in sorted(Country)))

