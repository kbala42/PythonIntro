print('''
-----------------------------------------------------------------------------tw:@tek_elo
Bir metinde geçip diğer metinde geçmeyen harfler
-----------------------------------------------------------------------------------------''')
metin1="""Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli 
bir programlama dilidir."""

metin2=" Python interaktif yani etkileşimli bir programlama dilidir!"

for i in metin2:
    if not i in metin1:
        print(i,end=",")
