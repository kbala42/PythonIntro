def n_Toplam(sayi):
    if sayi==1:
        return 1
    else:
         return sayi+n_Toplam(sayi-1)

sayi=int(input("Kaçıncı sayıya kadar toplam istiyorsunuz: "))
print("n sayının toplamı :", n_Toplam(sayi))

