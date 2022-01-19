print('----------------------------------------------------------tw:@tek_elo')
print('Dizi şeklinde Verilen sayıların toplamı\n'
      've ortalamalarını hesaplayan fonksiyon')
print('---------------------------------------------------------------------')
print()

# Fonksiyonu tanımlıyoruz
def sayilar(sayi):
    toplam=0 # toplam değişkenini tanımlıyoruz
    # uzunluğu hesaplayarak tek tek elemanları dolaşıyoruz
    for i in range(len(sayi)):
        toplam+=sayi[i] # o anki değerle önce ki değeri topluyoruz
    print("Toplam:",toplam)
    ortalama=toplam/len(sayi) # ortalamayı hesaplıyoruz
    print("Ortalama:",ortalama)

# Parametre şeklinde girilen sayılarla fonksiyonu çağırıyoruz
sayilar([1,2,3,4])

