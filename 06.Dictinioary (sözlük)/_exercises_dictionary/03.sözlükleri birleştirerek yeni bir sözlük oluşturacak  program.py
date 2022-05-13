"""
-------------------------------------------------------------------tw:@tek_elo

sözlükleri birleştirerek yeni bir sözlük oluşturacak bir Python programı yazın.

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# Python 3.9+ supports union operators for dictionaries:
# z = dic1 | dic2 | dic3
# print(z)

dic5 = {**dic1, **dic2, **dic3}
print(dic5)

dic6 = {}
for i in (dic1, dic2, dic3):
    for key, value in i.items():
        dic6[key] = value

print(dic6)