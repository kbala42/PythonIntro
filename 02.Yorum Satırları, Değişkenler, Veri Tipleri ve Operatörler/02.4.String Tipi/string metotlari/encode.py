print('--------------------------------------------------------')
print('encode() UTF-8 ile girilen metni çözümler')
print('--------------------------------------------------------')
metin = "İsmail, şükür kavuşturana"
print(metin.encode())
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.encode(encoding=encoding, errors=errors)
                 
        Parametre	        Tanım
        encoding	        Opsiyonel.Kodlamasistemi belirler. Varsayımda UTF-8 kodlama yapılır
        errors	            Opsiyonel. Metot hata yaptığında ne yapacağını belirler.
                
        ''')
print('--------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('backslashreplace: Kodlanamayan karakterin yerine ters slash işareti kullanır')
print('UTF-8 varsayım kodlama ')
print(metin.encode(errors="backslashreplace"))
print('ascii kodlama')
print(metin.encode(encoding="ascii",errors="backslashreplace"))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Ignore:Kodlanamayan karakterleri önemseme')
print('UTF-8 varsayım kodlama ')
print(metin.encode(errors="ignore"))
print('ascii kodlama')
print(metin.encode(encoding="ascii",errors="ignore"))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('namereplace:karakteri açıklama yazdırır')
print('UTF-8 varsayım kodlama ')
print(metin.encode(errors="namereplace"))
print('ascii kodlama')
print(metin.encode(encoding="ascii",errors="namereplace"))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('replace:Kodlanamayan karakteri soru işareti ile değiştirir')
print('UTF-8 varsayım kodlama ')
print(metin.encode(errors="replace"))
print('ascii kodlama')
print(metin.encode(encoding="ascii",errors="replace"))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('xmlcharrefreplace:Kodlanamayan karakteri bir xml karakteri ile değiştirir')
print('UTF-8 varsayım kodlama ')
print(metin.encode(errors="xmlcharrefreplace"))
print('ascii kodlama')
print(metin.encode(encoding="ascii",errors="xmlcharrefreplace"))
print('-----------------------------------------------------------------------')
print()