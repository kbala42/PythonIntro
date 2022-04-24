'''
---------------------------------------------------------tw:@tek_elo
Programımız verilen dizinin ortalamasını almaktadır. Ancak sonradan
tek ve çift sayılarında ortalamasını da ayrı ayrı hesaplayan
bir fonksiyonu yine decorate kullanarak ekliyoruz
--------------------------------------------------------------------
'''
def tekCiftOrtalama(fonk):

    def wrapper(sayilar):
        ciftlerToplami = 0
        ciftSayilar = 0
        teklerToplami = 0
        tekSayilar = 0

        for sayi in sayilar:

            if (sayi % 2 == 0):

                ciftlerToplami += sayi
                ciftSayilar +=1
            else:
                teklerToplami += sayi
                tekSayilar += 1

        print("Teklerin ortalaması:",teklerToplami/tekSayilar)
        print("Çiftlerinortalaması:", ciftlerToplami / ciftSayilar)

        fonk(sayilar)
    return wrapper

@tekCiftOrtalama
def ortalamaBul(sayilar):

    toplam = 0

    for sayi in sayilar:
        toplam += sayi
    print("Genel ortalama:",toplam/len(sayilar))

ortalamaBul([1,2,3,4,34,60,32,100,105])