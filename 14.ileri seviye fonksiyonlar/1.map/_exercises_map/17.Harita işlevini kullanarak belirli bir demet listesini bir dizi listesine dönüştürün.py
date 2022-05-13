"""
-------------------------------------------------------------------tw:@tek_elo

Harita işlevini kullanarak belirli bir demet listesini bir dizi listesine dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colors))
names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print("\nOriginal list of tuples:")
print(names)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(names))

