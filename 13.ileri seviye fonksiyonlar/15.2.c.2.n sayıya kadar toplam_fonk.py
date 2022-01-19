def n_Toplam(sayi):
    toplam=0
    for i in range(1,sayi+1):
        toplam+=i
    return toplam

sayi=int(input("Kaçıncı sayıya kadar toplam istiyorsunuz: "))
print("n sayının toplamı :", n_Toplam(sayi))

