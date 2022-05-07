'''
-------------------------------------------------------------------tw:@tek_elo

      ljust metodu stringi belirlenen sayı kadar sola yaslar

------------------------------------------------------------------------------
'''

txt = 'Python,' 
x = txt.ljust(20)
print(x, 'C#, Dart, Kodlin')
print()

''' 
------------------------------------------------------------------------------- 

Syntax
                 string.ljust(length, character)

        Parametre	        Tanım
        length 	            Zorunlu. Ayracı belirler varsayımda boşluktur
        character 	        Opsiyonel.Doldurmak için diz

         
-------------------------------------------------------------------------------
'''
sayi = '540' 
s = sayi.ljust(20,'0')
print(s)

