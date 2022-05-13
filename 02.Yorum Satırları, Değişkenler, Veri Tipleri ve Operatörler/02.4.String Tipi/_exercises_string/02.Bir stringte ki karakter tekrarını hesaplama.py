"""
-------------------------------------------------------------------tw:@tek_elo

Bir stringte ki karakter tekrarını hesaplayan program

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
metin = 'Pireli peynirle perhizli pireler tepelerse, pireli peynirle de pır pır pervaz ederler'

'''
1. çözüm
'''
harfler1 = []
sozluk1 = {}
for t in metin:
    anahtarlar = sozluk1.keys()
    if t in anahtarlar:
        sozluk1[t] += 1
    else:
        sozluk1[t] = 1

print(sozluk1)
print()

'''
2. çözüm
'''
harfler = []
adet = 0

def harfTekrariniSay(mtn):
    sozluk = {}
    for t in mtn:
        anahtarlar = sozluk.keys()
        if t in anahtarlar:
            sozluk[t] += 1
        else:
            sozluk[t] = 1
    return sozluk
print(harfTekrariniSay(metin))

