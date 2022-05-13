"""
-------------------------------------------------------------------tw:@tek_elo

Bir Enum nesnesi oluşturmak ve üye adını ve değerini görüntülemek için bir Python programı yazın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))

