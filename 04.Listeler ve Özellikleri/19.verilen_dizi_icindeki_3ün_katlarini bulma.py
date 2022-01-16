print('-------------------------------------------------------------@tek_elo')
print('Verilen dizide 3 tam bölünenleri bulsn program')
print('---------------------------------------------------------------------')
print()

sayilar_dizisi=[5,8,12,17,25,36,41,49,60,72]

for i in sayilar_dizisi:
    if i%3==0: # 3bölümünden kalanlar
        print(i)
