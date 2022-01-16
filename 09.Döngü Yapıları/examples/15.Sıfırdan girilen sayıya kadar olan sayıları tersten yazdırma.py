print('''
-----------------------------------------------------------------------------tw:@tek_elo
Sıfırdan girilen sayıya kadar olan sayıları tersten yazdırma
----------------------------------------------------------------------------------------''')

sayi=int(input("Sınır değeri giriniz:"))
for i in range(sayi,0,-1):
    print(i,end=",")