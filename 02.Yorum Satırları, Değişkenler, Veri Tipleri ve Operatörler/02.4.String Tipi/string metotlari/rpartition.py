'''
-------------------------------------------------------------------tw:@tek_elo

        rpartition metodu   belirlenen grup dahil olmak üzere 
                            öncesi ve sonrasını gruplayarak tuple döndürür

------------------------------------------------------------------------------
'''

txt = 'Kara kalem, defter, silgi var.'
print(txt.rpartition('defter'))

print('-----------------------------------------------------------------------')
print('Eğer parametre stringte yoksa')
print('1 Boş string ')
print('2 Boş string ')
print('3. dolu string olarak döndürür')
print('-----------------------------------------------------------------------')
print(txt.rpartition('cetvel'))