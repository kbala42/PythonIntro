print('------------------------------------------')
print('lstrip() fonksiyonu solda ki boşluğu siler')
print('------------------------------------------')
metin1 = '   Merhaba Python'
print(metin1.lstrip())
print()

print('-------------------------------------------')
print('Sol baş dışında ki harfler sonucu etkilemez')
print('-------------------------------------------')
metin2 = 'Kara Tren'
print(metin2.lstrip('ra'))

print('-------------------------------------------')
print('Sol baştan yazılan metin kırpılır----------')
print('-------------------------------------------')
metin3='Yemyeşil Otlar '
print(metin3.lstrip('Yem'))






