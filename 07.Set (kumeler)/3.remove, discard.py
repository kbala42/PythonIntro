print('----------------------------------------------------------tw:@tek_elo')
print('Setlerde eleman çıkartma')
print('---------------------------------------------------------------------')

print('----------------------------------------------------------')
print('removesilme yapar')
print('Ancak olmayan elemanda hata verir')
print('----------------------------------------------------------')
sayi={3,1,5,5,8,0,5,4}
print(sayi)
sayi.remove(3)
print(sayi)
#sayi.remove(3)
print()


print('----------------------------------------------------------')
print('discard silme yapar')
print('Olmayan bir elaman silinmeye kalkışırsa önemsenmez')
print('----------------------------------------------------------')
sayi.discard(5)
print(sayi)
sayi.discard(5)
print()

