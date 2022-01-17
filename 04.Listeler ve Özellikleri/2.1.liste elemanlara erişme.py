print('-------------------------------------------------------------@tek_elo')
print('Tanımlanmış veriler bütün veya parçalı şekillerde erişilebilir ')
print('---------------------------------------------------------------------')
print()

renkler = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

print('listeyi ekrana yazdırıyoruz')
print(renkler)
print()

print('listenin ilk verisine erişme')
print(renkler[0])
print()

print('listenin son verisine erişme')
print(renkler[6])
print()

print('2.elemen ve 4.eleman arası')
print(renkler[2:5])
print()

print('2.elemen ve 4.eleman arası yeni liste oluşturma')
ozelRenkler=renkler[2:5]
print(ozelRenkler)
print()

print('2.elemen ve sonrasına ulaşma')
print(renkler[2:])
print()

print('4.elemen ve öncesine ulaşma')
print(renkler[:5])
print()

print('2. ve 4. elemanlar arası elemanlara 2 şer atlayarak ulaşma')
print(renkler[2:5:2])
print()

print('son elemana ulaşma')
print(renkler[-1])
print()

print('tersten 5. elemana ulaşma')
print(renkler[-5])
print()

print('listeyi tersten yazdırma')
print(renkler[::-1])
