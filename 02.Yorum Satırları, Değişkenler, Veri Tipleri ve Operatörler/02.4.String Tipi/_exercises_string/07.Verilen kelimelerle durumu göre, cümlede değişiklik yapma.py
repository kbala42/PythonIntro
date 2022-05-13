"""
-------------------------------------------------------------------tw:@tek_elo
Belirli bir dizgeden 'not' ve 'poor' alt dizgisinin ilk görünümünü bulun,
'poor'i 'not' takip ediyorsa, tüm 'not'...'poor' alt dizgisini 'good' ile değiştirin.
Ortaya çıkan dizeyi döndürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""


def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

