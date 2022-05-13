"""
-------------------------------------------------------------------tw:@tek_elo

Bir enum sınıfı üzerinde yineleme yapın ve bireysel üyeyi ve değerlerini görüntüleyin

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
for data in Country:
    print('{:15} = {}'.format(data.name, data.value))
