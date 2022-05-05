print('----------------------------------------------------------tw:@tek_elo')
print('Setler(kümeler) tek bir değişkende birden çok elemanı\n'
      'saklamak için kullanılan yapılardır.\n'
      'setlerin özellikleri;\n'
      'setler değiştirilemez ancak yeni parçalar eklenebilir ve parçalar silinebilir\n'
      'setler sıralanamaz\n'
      'setler indekslenemez\n')
print('---------------------------------------------------------------------')
print()
print('----------------------------------------')
print('Setler kırlangıçlar arasında tanımalanır')
print('----------------------------------------')
sayi={3,1,5,5,8,0,5,4}
print(type(sayi))
print(sayi)
print()

print('--------------------------------------------------------')
print('Setlerde iki ve daha fazla eklenmiş elemanlar önemsenmez')
print('--------------------------------------------------------')
sayilar={1,2,3,8,1,1,5,3}
print(sayilar)
print()

print('--------------------------------------------------------')
print('Setler değişik veri tiplerinden yapılabilir')
print('--------------------------------------------------------')
mantiksal = {True, False, True}
stringTipi = {'Konya', 'İstanbul', 'Ankara'}
karisik = {'Konya', True, 1, 6.2}
print(mantiksal)
print(stringTipi)
print(karisik )
print()

print(stringTipi)
print(karisik )
print()

print('--------------------------------------------------------')
print('Setler liste, tuple, string\'ten oluşturulabilir')
print('--------------------------------------------------------')
liste = ['a', 1, 5, 1, 'b', 'a']
listeSet = set(liste)
print(listeSet)
print('-------------------------')

tuple = (1, 2, 3, 2, 'Mars')
tupleSet = set(tuple)
print(tupleSet)
print('-------------------------')

string = 'Merhaba_Dünya'
strinSet = set(string)
print(strinSet)
print('-------------------------')

