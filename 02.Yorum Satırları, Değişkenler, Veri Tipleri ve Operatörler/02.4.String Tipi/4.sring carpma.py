metin1 = 'Merhaba'
metin2 = 'Python'
# metin3=metin1*metin2 iki çarpılmaz

print('----------------------------------------------------------------------------------------')
print('---metin sabit bir sayı ile çarpılabilir. Bu durumda sabir kadar kendini tekrar eder.---')
print('----------------------------------------------------------------------------------------')
print(3*metin1)
print()

print('----------------------------------------------------------------------------------------')
print('----Kelimelerin tekrarında karışmayı önlemek için boşuk eklenebilir. -------------------')
print('----Eğer öncelik için parantes kullanılmazsa sonuç etkisiz olur-------------------------')
print('----------------------------------------------------------------------------------------')
print(3*metin1+' ')
print(3*(metin1+' '))