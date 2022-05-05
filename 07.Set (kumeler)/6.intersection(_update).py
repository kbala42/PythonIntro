print('----------------------------------------------------------tw:@tek_elo')
print('intersection metodu sayının karşılaştırılan sayı ile\n'
      'ortak olan elemanlarını bulur')
print('---------------------------------------------------------------------')
sayi1={3,1,5,5,8,0,5,4}
sayi2={5,6,15,0,3}

print(sayi1)
print(sayi2)
print(sayi1.intersection(sayi2))
print(sayi1 & sayi2)
print('-------------------------')
sayi1.intersection_update(sayi2)
print(sayi1)
