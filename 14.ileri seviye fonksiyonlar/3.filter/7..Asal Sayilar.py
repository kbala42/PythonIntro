'''
---------------------------------------------------------tw:@tek_elo
100'e kadar sayılar içindeki asal sayıları bulan program
--------------------------------------------------------------------
'''
# sayı asal mı?
def asalMi(x):
    sayac=2
    if (x==1):
        return False
    elif (x==2):
        return True
    else:

        while (sayac<x):
            if(x%sayac==0):
                sayac+=1
                return False

            return True
# 1-100 arası diziye asalMi fonksiyonunu uygula
# asla olanlarını listeye dönüştür
asalSayilar=list(filter(asalMi,range(1,100)))

#asalSayilar listesini yazdır
print(asalSayilar)