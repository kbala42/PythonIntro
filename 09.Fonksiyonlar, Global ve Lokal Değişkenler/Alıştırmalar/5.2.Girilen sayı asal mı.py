def AsalMi(sayi):
    sayac=2 # tüm sayılar 1'e bölüneceğinden 2 ile başlattık
    for i in range(2,int(sayi/2)):
        if sayi%sayac==0:
            return False
    return True
#Fonksiyonu çağırma
print(AsalMi(113))