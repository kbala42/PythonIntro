print('----------------------------------------------------------tw:@tek_elo')
print('İki demetten iki demet (tuple) oluşturma')
print('---------------------------------------------------------------------')
sayilar = (0,1,2,3,4,5,6,7,8,9,)
print(type(sayilar))
print()

harfler = ('a','b','c','d','e')
print(type(sayilar))
print()

print('İki demetten tek demet oluşturuyoruz')
karisikDemet = sayilar + harfler
print(type(karisikDemet))
print(karisikDemet)
print()

print('---------------------------------------------------------')
print('artım += operatörü kullanarak aynı tuple üretilir')
print('---------------------------------------------------------')
renkler = ('Kirmizi','Beyaz')
yeniRenkler = ('Kirmizi','Beyaz')
renkler += yeniRenkler
print(renkler)
print()

print('---------------------------------------------------------')
print('Çarpılan sayı kadar yeni bir demet toplamına müsade eder.')
print('---------------------------------------------------------')
indisler=('i','j','k')
yeniIndisler = indisler *2
print(yeniIndisler)
print()

print('---------------------------------------------------------')
print('Yine çarpım operatörü kullanarak aynı tuple üretilir')
print('---------------------------------------------------------')
indisler=('i','j','k')
indisler *= 2 # aynı tuple tekrar oluşturuluyor
print(indisler)
