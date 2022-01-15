print('--------------------------------------------------------------tw:@tek_elo')
print(' 1ile 100 ile yüz arasında ki sayıların toplamını ekrana yazdıran program')
print('-------------------------------------------------------------------------')

sayac=1 # saydırma değişkenimizi 1 den başlatıyoruz

toplam=0 # rakamların toplamını saklayacağımız değişken

while sayac<=100: # sayac 100 ve küçükse bloğu yürüt
    toplam+=sayac # o anki sayac içeriğini ile önce toplama ekle
    sayac+=1 # sayac değerini 1 arttır
print()
print(f'1 ile 100 arası sayıların toplamı:{toplam} ')


