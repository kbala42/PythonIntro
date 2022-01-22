'''
---------------------------------------------------------tw:@tek_elo
Fonksiyon çalışma zamanını hesaplama
Decorate fonksiyonun aslı bozulmadan yeni işlevselllik katılmasıdır.
Bunuda en iyi normal bir hesaplama ve decorate yapılmış şekli
karşılaştırılarak görebiliriz.
Programda 100000 kadar sayıların karesi ve küpünü hesaplamasını
ne kadar zamanda olduğunu gösteren programın normal algoritma ile çözümü
aşağıda yer alıyor.
--------------------------------------------------------------------
'''
import time
def kareleriHesapla(sayilar):
    #sonuc isminde boş liste oluşturuyoruz
    sonuc = list()
    #sayaç için zamanı başlatıyoruz
    baslama = time.time()
    # kareleri alarak istenen hesaplamayı yaparak listeye ekliyoruz
    for i in sayilar:
        sonuc.append(i ** 2)
    # bitiş zamanını alıyoruz
    bitis = time.time()
    #zamanı hesapladıktan sonra yazdırıyoruz
    print("Bu fonksiyon " + str(bitis-baslama) + "saniye sürdü.")
    # sonuç listesini döndürüyoruz
    return sonuc


def kupleriHesapla(sayilar):
    # sonuc isminde boş liste oluşturuyoruz
    sonuc = list()

    # sonuc isminde liste oluşturuyoruz
    baslama = time.time()

    # küpleri alarak istenen hesaplamayı yaparak listeye ekliyoruz
    for i in sayilar:
        sonuc.append(i ** 3)

    # bitiş zamanını alıyoruz
    bitis = time.time()

    # zamanı hesapladıktan sonra yazdırıyoruz
    print("Bu fonksiyon " + str(bitis - baslama) + "saniye sürdü.")

    # sonuç listesini döndürüyoruz
    return sonuc
# kareleriHesapla fonksiyonunu 0-100000 arası sayılar için çağırıyoruz
kareleriHesapla(range(100000))
# kupleriHesapla fonksiyonunu 0-100000 arası sayılar için çağırıyoruz
kupleriHesapla(range(100000))