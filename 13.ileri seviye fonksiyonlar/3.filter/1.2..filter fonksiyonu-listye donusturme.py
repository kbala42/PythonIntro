'''
---------------------------------------------------------tw:@tek_elo
tek sayılar dizisini yine listeye dönüştürerek işlem yapabiliriz
--------------------------------------------------------------------
'''
sonuc=filter(lambda x:x%2,[1,2,3,4,5,6,7,8] )

#filter nesnesini listeye dönüştürüyoruz
tekSayilar=list(sonuc)

#tekSayilar listesini yazdırıyoruz
print(tekSayilar)