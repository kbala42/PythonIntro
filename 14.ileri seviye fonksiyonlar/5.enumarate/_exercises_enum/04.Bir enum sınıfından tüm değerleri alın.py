"""
-------------------------------------------------------------------tw:@tek_elo

Bir enum sınıfından tüm değerleri alın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from enum import IntEnum
class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
country_code_list = list(map(int, Country))
print(country_code_list)

