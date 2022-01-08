def sayilar(sayi):
    toplam=0
    for i in range(len(sayi)):
        toplam+=sayi[i]
    print("Toplam:",toplam)
    ortalama=toplam/len(sayi)
    print("Ortalama:",ortalama)

sayilar([1,2,3,4])

