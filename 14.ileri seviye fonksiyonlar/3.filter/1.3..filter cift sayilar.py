'''
---------------------------------------------------------tw:@tek_elo
tek sayılar dizisini yine listeye dönüştürerek işlem yapabiliriz
--------------------------------------------------------------------
'''
# Sonuc true olanlarla filter nesnesi oluşturuyoruz
sonuc=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8] )

# filter nesnesini listeye dönüştürüyoruz
ciftSayilar=list(sonuc)

# listeyi yazdırıyoruz
print(ciftSayilar)