'''
-------------------------------------------------------------------tw:@tek_elo
    
    splitlines metodu stringi her yeni satır değerine göre böler
    
-------------------------------------------------------------------------------
'''
print()

txt = "Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli\n yüksek seviyeli bir programlama dilidir."
print(txt.splitlines())
print()

'''
-------------------------------------------------------------------------------
     Syntax
     
             string.splitlines(keeplinebreaks)
                 
        Parametre	        Tanım
        keeplinebreaks      Opsiyonel. Ayracın katılıp (False), katılmayacağını (True)
                            belirler. Varsayım False
                
    
-------------------------------------------------------------------------------
'''
print()

print(txt.splitlines(True))

