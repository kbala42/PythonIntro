print('-------------------------------------------------@tek_elo')
print('copy()  metodu kullanılarak')
print('--------------------------------------------------------')
sozluk= {1: 'Bir', 'Iki': 'Iki', (3, 4, 5): 'Samsun', 'Yeni': 'Şehir',
          (1, 2): (3+4j), 5: 'Kalem', 'renk': 'Turkuaz'}
yeniSozluk=sozluk.copy()
print(sozluk)
print(yeniSozluk)
print()

print('--------------------------------------------------------')
print('dict() inşa fonksiyonu kullanılarak')
print('--------------------------------------------------------')
yeniDictSozluk=dict(sozluk)
print(sozluk)
print(yeniDictSozluk)