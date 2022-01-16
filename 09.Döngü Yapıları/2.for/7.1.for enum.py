print('----------------------------------------------------------tw:@tek_elo')
print('enumarate fonksiyonu sıralamasını düşündüğümüz listeleri\n' 
      'sıralamak için kullanılır')
print('---------------------------------------------------------------------')
print()

print('----------------------------------------------------')
print('Aşağıda ki gibi bir sıralama da sayac+=1 unutulursa\n'
      'hata olabilir')
print('----------------------------------------------------')
liste=['elma','armut','karpuz']
sayac=1
for i in liste:
    print(sayac,i)
    sayac+=1
print()

print('----------------------------------------------------')
print('Aynı programı enumarete ile yaparsak\n'
      'sonuç tuple olarak sıralı şekilde döner\n'
      'Burada 1 başlatma sayısı.\n'
      'Kullanılmazsa varsayım olarak 0 dan başlar')
print('----------------------------------------------------')
liste=['elma','armut','karpuz']
for sayac, meyve in enumerate(liste,1):
    print(sayac,meyve)
print()

print('----------------------------------------------------')
print('Aşağıda ki kullanımda Tuple olarak döner')
print('----------------------------------------------------')
for i in enumerate(liste):
    print(i)
print()

print('----------------------------------------------------')
print('Nesne oluşturursak\n'
      'enumarate sınıfından bir nesne oluşur')
print('----------------------------------------------------')
enumarateListe=enumerate(liste)
print(type(enumarateListe))
print(enumarateListe) # nesnenin hafıza adresi
print(list(enumarateListe))