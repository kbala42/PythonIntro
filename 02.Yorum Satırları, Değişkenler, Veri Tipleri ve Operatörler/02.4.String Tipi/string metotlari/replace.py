'''
-------------------------------------------------------------------tw:@tek_elo

    replace metodu aranan aranan kelime ile belirlenen kelimeyi değiştirir

------------------------------------------------------------------------------
'''
print()

txt = "pireli peynirle perhizli pireler tepelerse, pireli peynirle de pır pır pervaz ederler"
print(txt.replace('pır','çır'))
print()

'''
------------------------------------------------------------------------------
        Syntax
                 string.replace(oldvalue, newvalue, count)

        Parametre	        Tanım
        oldvalue	        Zorunlu. Eski değer
        newvalue	        Zorunlu. Yeni değer
        count               Opsiyonel. Kaç kez değiştirilmesini isteyorsunuz?

        Başka bir şey belirtilmemişse, belirtilen ifadenin tüm tekrarları değiştirilecektir.
------------------------------------------------------------------------------
'''

print('------------------------------------------------------------------------------')
print('1 yeri değiştiriyoruz')
print(txt.replace('pireli','tahta kurulu',1))