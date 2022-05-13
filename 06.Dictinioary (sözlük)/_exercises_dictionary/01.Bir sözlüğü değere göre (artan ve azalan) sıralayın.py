"""
-------------------------------------------------------------------tw:@tek_elo

Bir sözlüğü değere göre (artan ve azalan) sıralayın 

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
'''
Çözüm

'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(dict(sorted(d.items(), key=lambda x: str(x[1]))))

'''
Çözüm

'''

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d.items()))
print(sorted(d.items(),key=lambda x:x[1]))
print(sorted(d.items(),reverse=True))
print(sorted(d.items(),key=lambda x:x[1],reverse=True ))

'''
Çözüm

'''

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})
print({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)})


'''
Çözüm

'''

import operator

sozluk = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Orjinal sözlük : ', sozluk)

degeriArtanSozluk = sorted(sozluk.items(), key=operator.itemgetter(1))

print('Değere göre artan sıralama: ', degeriArtanSozluk)

degeriAzalanSozluk = dict( sorted(sozluk.items(), key=operator.itemgetter(1),reverse=True))

print('Değere göre azalan sıralama: ',degeriAzalanSozluk )


'''
Çözüm

'''

def degerineGoreSirala(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

print("Orjinal sözlük:")
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print(colors)

print("\nDeğerine göre artan sırama:")
print(degerineGoreSirala(colors))

print("\nDeğerine göre azalan sırama:")
print(degerineGoreSirala(colors, True))


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
e = {}
for v in reversed(sorted(d.values())):
    for k in d:
        if d[k] == v and k not in e:
            e.update({k:v})
            print(e)