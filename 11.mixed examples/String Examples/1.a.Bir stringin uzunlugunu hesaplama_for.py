print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringin uzunluğunu hesaplayan program : for döngüsü ile
      ''')
print('---------------------------------------------------------------------\n')
str = 'Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir.'
count = 0

for i in str:
    count += 1

print('Stringin uzunluğu: ', count)

#programsız bulma
print('Stringin uzunluğu: ', len(str))
