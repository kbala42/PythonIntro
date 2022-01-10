print('-------------------------------------------------@tek_elo')
print('key e ait value değiştirerek')
print('--------------------------------------------------------')
sozluk= {1: 'Bir', 'Iki': 'Iki', (3, 4, 5): 'Samsun', 'Yeni': 'Şehir',
          (1, 2): (3+4j), 5: 'Kalem', 'renk': 'Turkuaz'}
sozluk[1]='one'
print(sozluk)
print()

print('----------------------------')
print('update metodu kullanılarak')
print('key:value girerek')
print('----------------------------')
sozluk.update({'Yeni':'Yaşam'})
print(sozluk)
print()
