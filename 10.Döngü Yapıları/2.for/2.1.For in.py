print('--------------------------------------------------------------tw:@tek_elo')
print(' For döngüsü liste, demet (tuple), küme(set), sözlük (dictionary), string\n'
      'içinde sıralı olarak dolaşmamızı sağlayan döngülerdir')
print('------------------------------------------------------------------------')
print()

print('----------------------')
print('string içinde kullanımı')
print('----------------------')
for i in 'konya':# string içinde ki harfleri tek tek yazdırıyoruz
    print(i)
print()

print('----------------------')
print('liste içinde kullanımı')
print('----------------------')
liste=[1,2,3,4,5,6]
for i in liste:# liste içinde ki harfleri tek tek yazdırıyoruz
    print(i)
print()

print('----------------------')
print('demet(tuple) içinde kullanımı')
print('----------------------')
demet=(5,'kalem',6,'silgi')
for i in demet:# liste içinde ki harfleri tek tek yazdırıyoruz
    print(i)
print()

print('-----------------------------------')
print('sözlük(dictionary) içinde kullanımı')
print('-----------------------------------')
sozluk={1:'One',2:'two'}
for i in sozluk:# sözlük içinde anahtarları tek tek yazdırıyoruz
    print(i)
print()

for i in sozluk.values():# sözlük içinde değerleri tek tek yazdırıyoruz
    print(i)
print()

print('----------------------')
print('küme(set) içinde kullanımı')
print('----------------------')
sayi={3,1,5,5,8,0,5,4}
for i in sayi:# liste içinde ki harfleri tek tek yazdırıyoruz
    print(i)
print()