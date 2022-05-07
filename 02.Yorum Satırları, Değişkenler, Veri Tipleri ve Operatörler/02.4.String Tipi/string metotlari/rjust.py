'''
-------------------------------------------------------------------tw:@tek_elo

      rjust metodu stringi belirlenen sayı kadar sağa yaslar 

------------------------------------------------------------------------------
'''

txt = 'Python,' 
x = txt.rjust(20)
print(x, 'C#, Dart, Kodlin')
print()

''' 
------------------------------------------------------------------------------- 

Syntax
                 string.rjust(length, character)

        Parametre	        Tanım
        length 	            Zorunlu. Ayracı belirler varsayımda boşluktur
        character 	        Opsiyonel.Doldurmak için diz

         
-------------------------------------------------------------------------------
'''
sayi = '540' 
s = sayi.rjust(20,'0')
print(s)

