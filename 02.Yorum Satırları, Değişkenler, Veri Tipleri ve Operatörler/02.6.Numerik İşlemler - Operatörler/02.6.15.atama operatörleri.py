print("*****************************")
print('Atama operatörü = ')
print("*****************************")
sayiBir = 5
sayiIki = sayiBir # sayiBir içeriği sayiIki'ye atanıyor
print('sayiBir = ',sayiBir)
print('sayiIki = ',sayiIki)
print()

print("*****************************")
print("Arttırma operatörü +=")
print("*****************************")
sayiBir = 5
print("Değişkenin içeriği ile artım sayısını toplayıp aynı değişkene atama yapıyoruz")
sayiBir += 3
print ('sayiBir += 3 : ',sayiBir)
print()

print("***********************************************************************")
print("Artım operatörünü string ile yaparsak iki metnin toplamı gibi çalışır")
print("***********************************************************************")
metinBir = 'Merhaba '
print('metin1=metin1+"Dünya" koduyla aynı işlevi görür.')
metinBir +='Dünya'
print('metinBir +=\'Dünya\' : ',metinBir)
print()

print("*****************************")
print("Çıkartım operatörü -= ")
print("*****************************")
sayiBir = 5
print("Değişkenin içeriğinden çıkartım sayısını toplayıp aynı değişkene atama yapıyoruz")
sayiBir -= 3
print('sayiBir -= 3 : ',sayiBir)
print()

print("*****************************")
print("Çarpim/Katlama operatörü = ")
print("*****************************")
sayiBir = 5
print("Değişkenin içeriğinden çarpim/Katlama sayısını çarpıp aynı değişkene atama yapıyoruz")
sayiBir *= 3
print('sayiBir *= 3 : ',sayiBir)
print()

print("***********************************************************************")
print('Aynı şekilde karakter dizilerini de çoğaltma için kullanabilirsiniz.')
print("***********************************************************************")
metinBir = 'Merhaba '
print('metin1=metin1*3 koduyla aynı işlevi görür.')
metinBir *= 3
print('metinBir *= 3 : ',metinBir)
print()

print("*****************************")
print("Bölen operatörü = ")
print("*****************************")
sayiBir = 6
print('sayiBir = sayiBir / 3 koduyla aynı işlevi görür.')
sayiBir /= 3
print('sayiBir /= 3 : ',sayiBir)
print()

print("*****************************")
print("Kuvet operatörü = ")
print("*****************************")
sayiBir = 5
print('sayiBir = sayiBir ** 3 ile aynı işlemi yapar')
sayiBir **= 3
print('sayiBir **= 3 : ',sayiBir)
print()

print("*****************************")
print("Bölüm operatörü = ")
print("*****************************")
sayiBir = 5
print('sayiBir = sayiBir // 3 ile aynı işlemi yapar')
sayiBir //= 3
print('sayiBir //= 3 : ',sayiBir)
print()

print("*****************************")
print("Kalan operatörü = ")
print("*****************************")
sayi1 = 5
print('sayiBir = sayiBir // 3 ile aynı işlemi yapar')
sayi1 %= 3
print('sayi1 %= 3 : ',sayi1)
print()

print("*****************************")
print("Tek satırda veri atama")
print("*****************************")
i, j, k = 1,2,3
print("i=", i)
print("j=", i)
print("k=", i)
print()

print("*****************************")
print("Veri içeriklerini değiştirme")
print("*****************************")
print("i=", i)
print("j=", j)
print("k=", k)
print()
i, j, k = j, k, i
print('i, j, k = j, k, i')
print('Yeni değerler')
print("i=", i)
print("j=", j)
print("k=", k)
print()