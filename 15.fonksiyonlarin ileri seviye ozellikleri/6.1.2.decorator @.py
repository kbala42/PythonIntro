'''
---------------------------------------------------------tw:@tek_elo
Programda 100000 kadar sayıların karesi ve küpünü hesaplamasını
ne kadar zamanda olduğunu gösteren programın decorate ile çözümü
aşağıda yer alıyor.
Programda hesaplama adımı ayrı bir fonksiyonla hesaplanıyor.
@ operatörü ile ölçülmesini istediğimiz fonksiyona ekliyoruz.
Bu sayede fonksiyonun aslı bozulmadan çalışıyorlar. Fonksiyon çağrıldığında
decorate içinde ama birlikte çalıştırılıyor.
--------------------------------------------------------------------
'''
import time

# decorate fonksiyonu: zaman hesaplama
def zamanHesapla(func):
    def wrapper(sayilar):
        baslama = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__+" " + str(bitis - baslama) + "saniye sürdü.")

        return sonuc
    return wrapper

#kareleriHesapla çağrıldığında önce zamanHesapla başlatıp
# hesaplama bittikten sonra zamanHesapla bittikten sonra işlem bitiyor
@zamanHesapla
def kareleriHesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 2)

    return sonuc

#kupleriHesaplaçağrıldığında önce zamanHesapla başlatıp
# hesaplama bittikten sonra zamanHesapla bittikten sonra işlem bitiyor
@zamanHesapla
def kupleriHesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 3)

    return sonuc

kareleriHesapla(range(100000))
kupleriHesapla(range(100000))