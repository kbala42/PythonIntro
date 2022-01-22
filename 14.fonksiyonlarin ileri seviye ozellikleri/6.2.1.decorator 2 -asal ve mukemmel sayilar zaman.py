'''
---------------------------------------------------------tw:@tek_elo
1'den 1000'e kadar olan asal sayıları  decorator fonksiyon kullanarak
ekrana yazdıran program
Fonksiyonumuz normalde asal sayıları hesaplıyor. Ancak sonradan
mükemmel sayı hesaplama özelliği de katıyoruz
--------------------------------------------------------------------
'''
import time

# decorate fonksiyonu: zaman hesaplama
def zamanHesapla(func):
    def wrapper(fonk):
        baslama = time.time()

        sonuc = func(fonk)

        bitis = time.time()

        print(func.__name__+" " + str(bitis - baslama) + "saniye sürdü.")

        return sonuc
    return wrapper
@zamanHesapla
def mukemmelSayi(fonk):
    def mukemmelSayiHesapla():
        print("__________1000 kadar mükemmel sayılar__________")
        for sayi in range(1, 1001):
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayi):
                print(sayi)
        fonk()

    return mukemmelSayiHesapla


@mukemmelSayi
def asalSayilar():
    print("__________1000 kadar asal sayılar__________")
    for sayi in range(2, 1001):
        i = 2
        say = 0
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayi)


asalSayilar()
