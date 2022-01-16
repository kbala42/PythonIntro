print('----------------------------------------------------------tw:@tek_elo')
print('Else anahtarsözcüğü for döngüsü bittikten sonra yürütülen bloktur')
print('---------------------------------------------------------------------')
for i in range(1,6):
    print(i)
else:
    print('Döngü bitti')
print()

print('---------------------------------------------------------------------')
print('Else, for döngüsü break ile sonlandırılırsa yürütülmez')
print('---------------------------------------------------------------------')
for i in range(1,6):
    if i==3:
        break
    print(i)
else:
    print('Döngü bitti')