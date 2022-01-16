print('''
-----------------------------------------------------------------------------tw:@tek_elo
Bir metinde geçen sesli harfler
-----------------------------------------------------------------------------------------''')
metin="""Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli 
bir programlama dilidir."""
sesli_harfler="aıioöuü"
sayac=0
for i in metin:
    if i in sesli_harfler:
        print(i,end=",")
