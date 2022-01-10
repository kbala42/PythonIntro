print('--------------------------------------------------------')
print('Boş sözlük nesnesi oluşturma - 1.yöntem\n'
      '1.Küme işareti/kırlangıç işareti ile')
print('--------------------------------------------------------')
sozlukBos1={}
print(type(sozlukBos1))
print(sozlukBos1)
print()

print('--------------------------------------------------------')
print('Boş sözlük nesnesi oluşturma - 2.yöntem\n'
      'dict() fonksiyonu kullanarak')
print('--------------------------------------------------------')
sozlukBos2=dict()
print(type(sozlukBos2))
print(sozlukBos2)
print()

print('--------------------------------------------------------')
print('Dolu Sözlük nesnesi oluşturma - k\n'
      'Anahtar ve değer çiftleri girerek')
print('--------------------------------------------------------')
sozlukKeyValue= {"Bir":1,"Iki":2,"Uc":4}
print(type(sozlukKeyValue))
print(sozlukKeyValue)
print()

print('-----------------------------------------------------------------')
print('dict inşa fonksiyonunun fronkeys() metodunu kullanarak oluşturma\n'
      '1. iki farklı diziden key-value çifti oluşturarak')
print('-----------------------------------------------------------------')
plakaNo = (16,34,42,77)
il = ('Bursa','İstanbul', 'Konya','Yalova')
plakaIl = dict.fromkeys(plakaNo, il)
print(plakaIl)
print()

