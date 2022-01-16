print('----------------------------------------------------------tw:@tek_elo')
print('Comprehensive listeden yeni bir liste üretmek için kullanırız\n'
      'Kopya liste oluştursaydık asıl liste yada kopyada ki değişiklik\n'
      'her iki listeyede aynen yansır')
print('---------------------------------------------------------------------')
print()

print('-----------------------------------------')
print('liste1 den kopyalama ile liste3\n'
      'comprensive liste2 oluşturuyoruz')
print('-----------------------------------------')
liste1=[1,2,3,4,5]
liste2=list() #Boş liste oluşturuyoruz
liste3=liste1 #Kopya liste
print(liste2) # boş listeyi yazdırıyoruz
for i in liste1:
    liste2.append(i)
print(liste2)
print()

print('----------------------------------------------------')
print('liste1 ve liste2 yeni elemanlar ekliyoruz\n'
      'Ekleme sonucunda her iki liste bağımsız hareket etti')
print('----------------------------------------------------')
liste1.append(9)
liste2.append(20)
print(liste1)
print(liste2)
print()

print('----------------------------------------------------')
print('Ancak liste1 ve liste3 yeni elemanlar eklediğimizde\n'
      'Her iki listeye aynı anda ekleme yapıldı')
print('----------------------------------------------------')
liste1.append(40)
liste3.append(100)
print(liste1)
print(liste3)

print('----------------------------------------------------')
print('Nesnelerin hafıza bölgelerini görüntüleme')
print('----------------------------------------------------')
print('liste1:',id(liste1))
print('liste3:',id(liste3))
print('--------------------')
print('liste2:',id(liste2))