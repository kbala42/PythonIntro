"""
-------------------------------------------------------------------tw:@tek_elo
Belirtilen karakterden önce bir dizenin son bölümünü almak için bir Python programı yazın.


-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])
