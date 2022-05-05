print('-------------------------------------------------@tek_elo')
print('popItem metodu kullanılarak')
print('son elmanı siler')
print('--------------------------------------------------------')
sozluk= {1: 'Bir', 'Iki': 'Iki', (3, 4, 5): 'Samsun', 'Yeni': 'Şehir',
          (1, 2): (3+4j), 5: 'Kalem', 'renk': 'Turkuaz'}
sozluk.popitem()
print(sozluk)
print()
sozluk.popitem()
print(sozluk)
print()

print('----------------------------')
print('pop metodu kullanılarak')
print('key girerek')
print('----------------------------')
sozluk.pop('Yeni')
print(sozluk)
print()

print('----------------------------')
print('del anahtar sözcüğü kullanılarak')
print('----------------------------')
del sozluk['Iki']
print(sozluk)

print('---------------------------------')
print('del sözcüğü tüm sözlüğü silebilir')
print('---------------------------------')
#del sozluk
#print(sozluk)

#del sozluk['Iki'] # Yanlışlıkla önceden silinen bir sözlük kullanılırsa
#print(sozluk)