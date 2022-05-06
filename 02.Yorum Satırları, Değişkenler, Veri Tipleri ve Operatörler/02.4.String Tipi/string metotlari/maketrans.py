'''
--------------------------------------------------------------tw:@tek_elo

maketrans metodu bir karakter yerine diğer karakteri yerleştirir

kendisi unicode olarak değiştireceğini belirler.

Çevirme işlemi için translate metodundan faydalanılır

--------------------------------------------------------------- -------
'''
metin = "İsmail, şükür kavuşturana"
print(metin.maketrans('şü','us'))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.maketrans(x, y, z)

        Parametre	        Tanım
        x   	            Zorunlu. Yalnızca bir parametre belirtilirse, bu, değiştirmenin nasıl gerçekleştirileceğini 
                            açıklayan bir sözlük olmalıdır. İki veya daha fazla parametre belirtilmişse, bu parametre, 
                            değiştirmek istediğiniz karakterleri belirten bir dize olmalıdır.
        y	                Opsiyonel. x parametresiyle aynı uzunlukta bir dize. İlk parametredeki her karakter, bu 
                            dizideki karşılık gelen karakterle değiştirilecektir.
        z                   Opsiyonel. Orijinal dizeden hangi karakterlerin kaldırılacağını açıklayan bir dize.  

        ''')
print('--------------------------------------------------------')
print()

mtn = metin.maketrans('şü','su')
print(metin.translate(mtn))

print('-----------------------------------------------------------------------')
print('z parametresi kaldırılacak değeri belirler')
x, y, z = 'şü','su','İsmail,'
mtn = metin.maketrans(x, y, z)
print(metin.translate(mtn))
print('-----------------------------------------------------------------------')
print()
