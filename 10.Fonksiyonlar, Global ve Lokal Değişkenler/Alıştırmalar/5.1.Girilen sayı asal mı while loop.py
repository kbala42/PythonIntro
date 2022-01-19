print('----------------------------------------------------------tw:@tek_elo')
print('Girilen sayı asal mı olduğunu while döngüsü ile bulan fonksiyon')
print('---------------------------------------------------------------------')
print()
def AsalMi(sayi):
    sayac=2 # tüm sayılar 1'e bölüneceğinden 2 ile başlattık
    while sayac<=int(sayi/2):
        if sayi%sayac==0:
            return False
        sayac+=1
    return True
#Fonksiyonu çağırma
print(AsalMi(113))