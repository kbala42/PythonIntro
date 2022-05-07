'''
-------------------------------------------------------------------tw:@tek_elo

      rsplit metodu stringi boşlukla izlenen virgüller şeklinde 
                    bir listeye böler  

------------------------------------------------------------------------------
'''

txt ='Python, C#, Dart, Kodlin'
print(txt.rsplit(', '))
print()

''' 
------------------------------------------------------------------------------- 

Syntax
                 string.rsplit(separator, maxsplit)

        Parametre	        Tanım
        separator  	        Opsiyonel. Ayracı belirler varsayımda boşluktur
        maxsplit  	        Opsiyonel. Max ayrlacak sayıyı belirler

         
-------------------------------------------------------------------------------

'''
print(txt.rsplit(', ', 1))