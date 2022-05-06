print('------------------------------------------')
print('rstrip() metodu sagda ki boşluğu siler')
print('------------------------------------------')
metin1 = ' Python       '
x=metin1.rstrip()
print('Merhaba', x, ' Dili')
print()

print('-------------------------------------------')
print('Sağ baş dışında ki harfler sonucu etkilemez')
print('-------------------------------------------')
metin2 = 'Merhaba, Python, Dili'
print(metin2.rstrip('Python'))
print()

print('-------------------------------------------')
print('sağ baştan yazılan metin kırpılır----------')
print('-------------------------------------------')
metin3='Merhaba, Python, Dili'
print(metin3.rstrip(', Dili'))
print()

print('-------------------------------------------')
print('sağ baştan yazılan metin içinde ki karakterler kırpılır----------')
print('-------------------------------------------')
metin4 = '...,,,merhaba,,,,,,kyn.....'
x = metin4.rstrip('nky.,')
print(x)
print()

metin5 = 'www.deneme.com.tr/alt'
x = metin5.rstrip('/alt')
print(x)

