print('''
-----------------------------------------------------------------------------tw:@tek_elo
Girilen sayıya kadar sayıların toplamını bulma
----------------------------------------------------------------------------------------''')
toplam=0
sayi=int(input("Sınır değeri giriniz:"))
for i in range(sayi+1):
    toplam=toplam+i
print("girdiğiniz sayıların toplamı:",toplam)


