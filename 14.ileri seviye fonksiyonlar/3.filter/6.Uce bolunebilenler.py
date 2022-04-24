'''
---------------------------------------------------------tw:@tek_elo
Verilen dizide 3 tam olarak bölünenlerini bulan program
--------------------------------------------------------------------
'''
# sayilar listesi oluşturuyoruz
sayilar = [10, 15, 4, 29, 402, 249, 210, 55, 40, ]

# 3 e tam bölünenleri ile sonuc nesnesi üretiyoruz
sonuc = filter(lambda x: (x % 3 == 0), sayilar)

#sonuc nesnesinin içeriği
print("üç ile bölünebilenler:",*sonuc)

