"""
-------------------------------------------------------------------tw:@tek_elo

Sözlüğe bir anahtar ekleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
'''
Çözüm 1
'''
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

'''
Çözüm 2
'''
d[3]=50
print(d)