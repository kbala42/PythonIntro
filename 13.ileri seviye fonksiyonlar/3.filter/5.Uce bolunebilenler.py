sayılar = [10, 15, 4, 29, 402, 249, 210, 55, 40, ]
sonuc = filter(lambda x: (x % 3 == 0), sayılar)
print("üç ile bölünebilenler",*sonuc)

