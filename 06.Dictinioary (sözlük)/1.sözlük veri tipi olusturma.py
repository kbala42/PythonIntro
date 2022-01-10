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
      '1. Boş bir sözlük oluşturma')
print('-----------------------------------------------------------------')
anahtarlar = ('x','y','z')
anahtar = dict.fromkeys(anahtarlar)
print(anahtar)
print()

print('-----------------------------------------------------------------')
print('dict inşa fonksiyonunun fronkeys() metodunu kullanarak oluşturma\n'
      '2. Bütün değerleri 0 olan sözlük oluşturma')
print('-----------------------------------------------------------------')
anahtarlar = ('x','y','z')
deger=0
anahtar = dict.fromkeys(anahtarlar, deger)
print(anahtar)
print()
deger='sabit'
anahtar = dict.fromkeys(anahtarlar, deger)
print(anahtar)

print('-----------------------------------------------------------------')
print('dict inşa fonksiyonunun fronkeys() metodunu kullanarak oluşturma\n'
      '3. value bir liste olursa liste eklemeleri dictionary eklenir')
print('-----------------------------------------------------------------')
no = (16,34,42,77)
liste =[1]
noListe = dict.fromkeys(no, liste)
print(noListe)
print()
liste.append(2)
print(noListe)
print()
liste.append('boyut')
print(noListe)
print()

print('-----------------------------------------------------------------')
print('dict inşa fonksiyonunun fronkeys() metodunu kullanarak oluşturma\n'
      '4. Bütün değerleri döngü ile sözlük oluşturma')
print('-----------------------------------------------------------------')
anahtarlar = {1,2,3}
deger='x'
anahtarDongu = {anahtar: list(deger) for anahtar in anahtarlar}
print(anahtarDongu)
print()
