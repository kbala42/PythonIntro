print('----------------------------------------------------------tw:@tek_elo')
print('Comprehensive ile n ile çarpımı şeklinde yapılabilir')
print('---------------------------------------------------------------------')
liste1=[1,2,3,4,5]

liste2=list()

liste2=[i*2 for i in liste1]
print(liste2)
print()

print('liste2:',id(liste2))
print('--------------------')
print('liste1:',id(liste1))