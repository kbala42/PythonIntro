print('----------------------------------------------------------tw:@tek_elo')
print('Setlerde update metodu eleman ekleme için kullanılır')
print('---------------------------------------------------------------------')
sayi1={3,1,5,5,8,0,5,4}
print(sayi1)
print()

sayi2={10,6,15,0}
sayi1.update(sayi2)
print(sayi1)

print('-------------------------------------------')
print('Setler diğer list, tuple ve dictionary ile\n'
      'update yapılabilir')
print('-------------------------------------------')
sayi3=('x','y',8,15)
sayi1.update(sayi2)
print(sayi1)