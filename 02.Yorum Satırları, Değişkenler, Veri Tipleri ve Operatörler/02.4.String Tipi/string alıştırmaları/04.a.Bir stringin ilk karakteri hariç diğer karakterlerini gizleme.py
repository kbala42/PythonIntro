"""
-------------------------------------------------------------------tw:@tek_elo
Bir stringin ilk karakteri hariç diğer karakterlerini '*' işareti ile değiştiren program
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

kelime = 'Python'
harf0 = kelime[0]
for k in kelime:
    kelime = kelime.replace(k,'*')
print(harf0+kelime[1:])

