"""
-------------------------------------------------------------------tw:@tek_elo
for döngülerini kullanarak sözlükler üzerinde yineleme
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)


d = {'x': 10, 'y': 20, 'z': 30}
for i, j in zip(d.keys(),d.values()):
    print(i,"->",j)
    
for k,v in d.items():
    print('key: {0},  value: {1}'.format(k,v))

for i in d:
    print(i, ':', d[i])