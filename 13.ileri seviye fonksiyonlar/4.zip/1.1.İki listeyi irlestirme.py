'''
---------------------------------------------------------tw:@tek_elo
iki farklı listeyi elman sayılarını gözönünde tutarak birleştirilebilir
--------------------------------------------------------------------
'''
liste1=[3,9,2,5]
liste2=[8,21,50,5,1,7,4,]
# liste1 ve liste2 içinde gezinmek için sayaç değişkeni tanımlıyoruz
i=0
# sonuc isminde boş liste liste tanımlıyoruz
sonuc=list()
# liste1 ve liste2 aynı indis ise sonuc listesine ekle
while (i<len(liste1) and i<len(liste2)):
    sonuc.append((liste1[i],liste2[2]))
    i += 1
#sonuc listesini yazdır
print(sonuc)
