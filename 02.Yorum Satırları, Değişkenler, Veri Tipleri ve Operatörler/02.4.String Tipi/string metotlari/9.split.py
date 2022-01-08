print('------------------------------------------------------')
print('split metodu karakter dizisini liste haline dönüştürür')
print('------------------------------------------------------')
metin='Merhaba Python Dili'
print(metin.split())
print()

print('------------------------------------------------------------')
print('split metodunda ayıraç kulanırsa dönüşümü ayıraca göre yapar')
print('------------------------------------------------------------')
metin='Merhaba, Python Dili, Selam'
print(metin.split(', '))
print()

print('----------------------------------------------------')
print('# işareti burada eleman ayırması için kullanılabilir')
print('----------------------------------------------------')
metin='Merhaba#Python Dili#Selam'
print(metin.split('#'))
print()

metin='T.B.M.M'
print(metin.split('.'))
print()

metin='C:\\Users\\kbala\\Documents\\GitHub\\PythonIntro\\01.Hello Python\\1.1.Hello Python.py'
print(metin.split('\\'))
print()

print('------------------------------------------------------------')
print('split metodunda ayıraç kulanırsa dönüşümü ayıraca göre yapar')
print('------------------------------------------------------------')
metin='Merhaba, Python Dili, Selam'
print(metin.split(', '))
print()

print('----------------------------------------------------------------------------------')
print('Eğer split metodunda ayıraçla birlikte sayı girilirse max ayırma sayısı belirlenir')
print('----------------------------------------------------------------------------------')
metin='Merhaba, Python Dili, Selam'
print(metin.split(', ', 1))
print()