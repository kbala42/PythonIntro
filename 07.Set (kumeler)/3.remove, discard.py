print('----------------------------------------------------------tw:@tek_elo')
print('Setlerde eleman çıkartma')
print('---------------------------------------------------------------------')

sayi={3,1,5,5,8,0,5,4}
print(sayi)
sayi.discard(3)
print(sayi)
print()

print('--------------------------------------------------')
print('Olmayan bir elaman silinmeye kalkışırsa önemsenmez')
print('--------------------------------------------------')
sayi.remove(9)
print(sayi)
print()

print('--------------------------------------------------')
print('Parametresiz kullanılırsa önemsenmez')
print('--------------------------------------------------')
sayi.remove()
print(sayi)