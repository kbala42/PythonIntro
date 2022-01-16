print('----------------------------------------------------------tw:@tek_elo')
print('iç içe liste ve türevlerini for döngüsü ile alabiliriz')
print('---------------------------------------------------------------------')
print()

liste = [[3,4],[7,8],[10,11],[14,15]]

print('-----------------------------------------')
print('listeyi oluşturan elemanları yazdırıyoruz')
print('-----------------------------------------')
for i in liste:
    print(i)
print()

print('------------------------------------------------')
print('listenin içinde bulunan alt listelere ulaşıyoruz')
print('------------------------------------------------')
for i,j in liste:
    print(i,j)
print()

print('------------------------------------------------------')
print('listenin içinde bulunan alt listelere tekli ulaşıyoruz')
print('------------------------------------------------------')
for i in liste:
    for j in i:
        print(j)
