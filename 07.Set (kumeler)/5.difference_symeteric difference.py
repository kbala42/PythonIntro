print('----------------------------------------------------------tw:@tek_elo')
print('difference metodu sayının karşılaştırılan sayıdan\n'
      'farklı olan elemanlarını bulur')
print('---------------------------------------------------------------------')
sayi1={3,1,5,5,8,0,5,4}
sayi2={5,6,15,0,3}

print(sayi1)
print(sayi2)
print('-----------------------------------')
print(sayi1.difference(sayi2))
print(sayi2.difference(sayi1))
print('----------ortak olmayanlar---------')
print(sayi1.symmetric_difference(sayi2))
print(sayi2.symmetric_difference(sayi1))
print('-----------------------------------')
print(sayi1-sayi2)
print(sayi2-sayi1)