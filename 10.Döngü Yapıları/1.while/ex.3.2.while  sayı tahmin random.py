print('--------------------------------------------------------------tw:@tek_elo')
print(' 1 ile 100 ile yüz arasında rastgele tutlan sayının\n'
      'kaç tahminde bulduğunuzu ekrana yazdıran program')
print('-------------------------------------------------------------------------')
print()
from random import randint # random kitaplığından ranint modülünü alıyoruz
sayi=randint(1,100) # tahmin edilmesini istediğimiz sayı
                    # 1 ile 100 arasında rastgele sayı üretiyoruz
print(f'Programı denemek için tutlan sayıyı yazdıryoruz: {sayi}')
print()

sayac=0 # kaç tahminde bulunduğunu hesaplayan sayaç değişkeni
print('1-100 arası bir sayı tuttum tahmin et')

while 1==1: # true olduğu sürece sonsuz döngü

    sayac+=1 # Birinci tahmine başladığımız için burada artıma başlıyoruz
    cevap=int(input("1-100 arası bir sayı girin: ")) # Kullanıcının girdiği sayıyı tam sayıya dönüştürüyoruz
    if cevap>sayi:# eğer tahmin sayıdan büyükse
        print("daha küçük bir sayı girmelisin")
    elif cevap<sayi:# eğer tahmin sayıdan küçükse
        print("daha büyük bir sayı girmelisin")
    else: # eğer tahmin sayıya eşitse
        break # sonuç tahmin edilen sayıya eşitse döngüden çıkıyoruz
print()
print('tebrikler {} seferde sayıyı bulabildin'.format(sayac)) # tahmin adedini ekrana yazırıyoruz