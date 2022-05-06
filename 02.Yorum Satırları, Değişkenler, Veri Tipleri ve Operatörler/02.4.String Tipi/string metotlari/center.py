print('--------------------------------------------------------')
print('center() metodu girilen parametre kadar sayıyı sağdan \n'
      've soldan boşluk bırakılmasını sağlar.')
print('--------------------------------------------------------')
metin = 'Python'
print(metin.center(20))
print()

metin = 'Python'
print('Merhaba',metin.center(20),'Dili')
print()

print('--------------------------------------------------------')
print('center() metodunda varsayım boşultur.\n'
      'Eğer bir karakter verirse onunla doldurur')
print('--------------------------------------------------------')
metin = 'Python'
print('Merhaba',metin.center(20,'.'),'Dili')
print()

ayrac='_'
metin = 'Python'
print('Merhaba',metin.center(20,ayrac),'Dili')
print()