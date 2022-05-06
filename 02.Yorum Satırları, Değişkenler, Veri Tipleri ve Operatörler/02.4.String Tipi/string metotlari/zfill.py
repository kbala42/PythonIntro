'''
-------------------------------------------------------------------tw:@tek_elo
    zfill metodu verilen dizinin uzunluğuna göre stringin soluna eksik rakam kadar
          sıfır ekler
-------------------------------------------------------------------------------
'''
print()

txt = '287'
print(txt.zfill(7))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.zfill(len)
                 
        Parametre	        Tanım
        len	                Zorunlu. Stringin olmasını istediğiniz uzunluğu
                
        ''')
print('--------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')
txt1 = '189567'
print(txt1.zfill(3))
txt2 = '10.005'
print(txt2.zfill(3))
txt3 = 'Ali'
print(txt3.zfill(5))
txt2 = '10.5'
print(txt2.zfill(7))
print('-----------------------------------------------------------------------')
print()

