'''
-------------------------------------------------------------------tw:@tek_elo

        partition metodu   belirlenen grup dahil olmak üzere
                            öncesi ve sonrasını gruplayarak tuple döndürür

------------------------------------------------------------------------------
'''

txt = 'Kara kalem, defter, silgi var.'
print(txt.partition('defter'))

print('-----------------------------------------------------------------------')
print('Eğer parametre stringte yoksa')
print('1. dolu string olarak döndürür')
print('2 Boş string ')
print('3 Boş string ')


print('-----------------------------------------------------------------------')
print(txt.partition('cetvel'))