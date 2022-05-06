'''
-------------------------------------------------------------------tw:@tek_elo

translate metodu bir haritalama tablosu yada sözlükte tanımlanan karakterleri
                 belirlenen karakter yada karakterle değiştirmeye yarar

Haritalama tablosu için maketrans metodundan faydalanılır

-------------------------------------------------------------------------------
'''
print('Tek karakter')
metin = "İsmail, şükür kavuşturana"
print(metin.maketrans('ş','s'))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.translate(table)

        Parametre	        Tanım
        table  	            Zorunlu. Yerleştirmenin nasıl olacaüını belirleyen
                            harita yada sözlük

        ''')
print('--------------------------------------------------------')
print()
print('Çoklu karakter')
mtn = metin.maketrans('şü','su')
print(metin.translate(mtn))

print('-----------------------------------------------------------------------')
print('z parametresi kaldırılacak değeri belirler')
x, y, z = 'şü','su','İsmail,'
mtn = metin.maketrans(x, y, z)
print(metin.translate(mtn))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Sözlük kullanma')
print(metin.maketrans('İşü','Isu'))
mydict = {304: 73, 351: 115, 252: 117}
print(metin.translate(mydict))
print('-----------------------------------------------------------------------')
print()