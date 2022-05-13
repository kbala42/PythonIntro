"""
-------------------------------------------------------------------tw:@tek_elo

Harita işlevini kullanarak belirli bir dizi listesini liste listesine dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print('Original list of strings:')
print(colors)
print("\nConvert the said list of strings into list of lists:")
print(strings_to_listOflists(colors))

