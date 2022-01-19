print('----------------------------------------------------------tw:@tek_elo')
print('Random modülü rastgele sayılar üretmek için kullandığımız bir modüldür')
print('---------------------------------------------------------------------')
print()

import random

sayiBir=random.random() # Rastgele sayı üretiyoruz
print("0 ile 1 arasında rastgele sayı:",sayiBir)

sayiIki=random.randint(1,10) # Rastgele 1 ile 10 arasında bir sayı üretiyoruz
print("1 ile 10 arasında rastgele sayı:", sayiIki)

print("\n1 ile 10 arasında rastgele 3 sayı edinme",)
for i in range(3):
    sayi_3 = random.randint(1, 10)
    print(i,". sayi:",sayi_3)

print("\n1 ile 10 arasında rastgele 3 sayı edinme : son değer yok",)
for i in range(3):
    sayi_3 = random.randrange(1, 10)
    print(i,". sayi:",sayi_3)

gunler=("pazartesi","salı","çarşamba","perşembe","cuma")
print(random.choice(gunler))