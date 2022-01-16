print('''
-----------------------------------------------------------------------------tw:@tek_elo
Metinde geçen boşlukları silen program
-----------------------------------------------------------------------------------------''')
metin="m e r h a b a"
metin2=""
for i in metin:
    if i!=" ":
        print(i,end="")
print()

print('''
--------------------------------------
Boşlukları kaldırarak string oluşturma
--------------------------------------''')
metin3="y a l o v a"
metin4=""
for i in metin3:
    if i != " ":
        metin4+=i
print(metin4)
