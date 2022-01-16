print('''
-----------------------------------------------------------------------------tw:@tek_elo
Bir listedeki sayıların  ortalamalarını bulan program
-----------------------------------------------------------------------------------------''')
sayılar = [1,2,3,4,5,6,7,8,9]
toplam=0
for i in sayılar:
    toplam+=i
print("sayıların ortalaması: ",toplam/len(sayılar))