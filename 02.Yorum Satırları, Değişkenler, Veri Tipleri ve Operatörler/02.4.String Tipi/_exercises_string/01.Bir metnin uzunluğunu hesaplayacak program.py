'''
-------------------------------------------------------------------tw:@tek_elo
Bir metnin uzunluğunu hesaplayacak program yazın
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
'''
txt = 'Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.'

'''
1. solution
'''
print('Metnin uzunluğu 1. çözüm: ',len(txt))
print()
'''
2. solution
'''
count1 = 0
for i in txt:
    count1 += 1
print('Metnin uzunluğu 2. çözüm: ', count1)
print()

'''
3. solution
'''
def uzunlukHesapla(text):
    count2 = 0
    for i in text:
        count2 +=1
    return count2

print('Metnin uzunluğu 3. çözüm: ', uzunlukHesapla(txt))
print()