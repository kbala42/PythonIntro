print('''
-----------------------------------------------------------------------------tw:@tek_elo
 Bir metinde genen bir harfin sayısı
-----------------------------------------------------------------------------------------''')
metin="""Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir programlama dilidir."""
harf="a"
sayac=0
for i in metin:
    if i == harf:
        sayac +=1

print(f"metinde ki {harf} harf sayısı {sayac} adettir ")
