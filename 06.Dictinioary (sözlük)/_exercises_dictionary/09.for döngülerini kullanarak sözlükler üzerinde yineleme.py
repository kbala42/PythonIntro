"""
-------------------------------------------------------------------tw:@tek_elo

for döngülerini kullanarak sözlükler üzerinde yineleme

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 
