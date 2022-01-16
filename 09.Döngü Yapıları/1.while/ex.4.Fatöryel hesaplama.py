print('--------------------------------------------------------------tw:@tek_elo')
print(' Girilen sayının faktöryelini hesaplayan program')
print('-------------------------------------------------------------------------')
sayac=1 # sayaç değişkeni

sayi=int(input("faktöriyeli alınacak sayıyı giriniz: ")) # faktöryelini bulacağımız sayıyı kullanıcıdan alıyoruz

sonuc=1 # faktöryeli hesaplarken o anki çarpım sonucunu saklayacağımız değişken

while sayac<=sayi: # o anki sayaç değişkeni kullanıcının gireceği sayıdan küçük ve eşitse bloğu yürüt
    sonuc=sonuc*sayac
    sayac+=1
print(f'{sayi} sayısının faktöryeli: {sonuc}')