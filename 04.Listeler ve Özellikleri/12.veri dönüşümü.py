print('-------------------------------------------------------------@tek_elo')
print('Veri dönüşümü')
print('---------------------------------------------------------------------')
print()
liste=[1,2,3,4,5,'ankara']
print(liste)
print()

print('Verilen indisteki eleanı değiştiriyoruz')
liste[0]=str("kocaeli")
liste[2]=float(1.5)
liste[5]=int(20)
print(liste)
print()

print('string giriyoruz')
meyve="elma"
print (meyve)
print()

print('stringi listeye dönüştürüyoruz')
liste2=list(meyve)
print(liste2)
print()

print('verilen aralıkta liste oluşturuyoruz')
liste3=list(range(1,15,2))
print(liste3)
print()

print('listeyi sıralıyoruz')
liste3.sort()
print(liste3)
print()

print('listeyi ters çeviriyoruz')
liste.reverse()
print(liste)
print()

print('bir string tanımlıyoruz')
cumle="23 nisan herkese mutlu olsun"
print('Boşuklara göre yeni liste oluşturuyoruz')
kelimeler=cumle.split(" ")
print(kelimeler)
print('kelimeler listesinde ki eleman sayısı')
print("cümlenizde ",len(kelimeler),"adet kelime vardır")
print()

bilgi=input("bilgilerinizi araya virgül koyarak yazınız: ")
liste=bilgi.split(",")
print(liste)