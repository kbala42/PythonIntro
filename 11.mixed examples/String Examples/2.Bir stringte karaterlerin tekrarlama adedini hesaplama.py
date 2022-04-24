print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringte karaterlerin tekrarlama adedini hesaplayan program 
      ''')
print('---------------------------------------------------------------------\n')

def strFrequence(str):
    sozluk = {}
    for n in str:
        anahtarlar = sozluk.keys()
        if n in anahtarlar:
            sozluk[n] += 1
        else:
            sozluk[n] = 1
    return sozluk

str = 'Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir.'

print(str, '\nstringinin harf tekrarlama adetleri:')

print(strFrequence(str))

