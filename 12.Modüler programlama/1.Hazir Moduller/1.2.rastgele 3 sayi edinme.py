print('----------------------------------------------------------tw:@tek_elo')
print('Rastgele n adet sayı bulan program ')
print('---------------------------------------------------------------------')
print()

import random

print("\n1 ile 10 arasında rastgele 3 sayı edinme",)
for i in range(3):
    sayi_3 = random.randint(1, 10)
    print(i,". sayi:",sayi_3)

print("\n1 ile 10 arasında rastgele 3 sayı edinme : son değer dahil değil",)
for i in range(3):
    sayi_3 = random.randrange(1, 10 )
    print(i,". sayi:",sayi_3)

gunler=("pazartesi","salı","çarşamba","perşembe","cuma")
print(random.choice(gunler))