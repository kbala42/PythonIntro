print('-------------------------------------------------@tek_elo')
print('Bütün value degerlerini yazdırma')
print('--------------------------------------------------------')
sozluk1= {1:"Bir",'Iki':'Iki',(3,4,5):'Samsun' }
print(sozluk1.values())
print()

print('-------------------------------------')
print('sözlük key girerek value ulaşılabilir')
print('-------------------------------------')
print(sozluk1[1])
print(sozluk1['Iki'])
print(sozluk1[(3,4,5)])
print()

print('-------------------------------------')
print('sözlük key değerlerini get metodu\n '
      'parametresi olarak girip value ulaşılabilir')
print('-------------------------------------')
print(sozluk1.get(1))
print(sozluk1.get('Iki'))
print(sozluk1.get((3,4,5)))