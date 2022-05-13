"""
-------------------------------------------------------------------tw:@tek_elo

Harita işlevini kullanarak verilen dizelerin listesini ayrı ayrı listeleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 
print("\nAfter listify the list of strings are:") 
result = list(map(list, color)) 
print(result)
