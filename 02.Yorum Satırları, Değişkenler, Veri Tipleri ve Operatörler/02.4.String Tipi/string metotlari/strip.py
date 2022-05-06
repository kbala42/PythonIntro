'''
-------------------------------------------------------------------tw:@tek_elo
    strip metodu verilen dizinin başında ki ve sonundaki boşlukları kaldırı
-------------------------------------------------------------------------------
'''
print()

txt = '    226     '
kod = txt.strip()
print('Yalova telefonları ', kod, ' ile başlar')
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.strip(characters)
                 
        Parametre	        Tanım
        characters          Zorunlu. Kaldırılacak karakterler
                
        ''')
print('--------------------------------------------------------')
print()
txt = '*226xxxyyzz'
kod = txt.strip('*xyz')
print(kod)

