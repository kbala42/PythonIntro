'''
---------------------------------------------------------tw:@tek_elo
filter fonksiyonunun string uygulamaları
--------------------------------------------------------------------
'''
# verilen listede @ geçenler
liste=["aa@a","123"]
sonuc=filter(lambda kelime:"@" in kelime, liste)
print(*sonuc)

# verilen listede @ geçenler
# liste=["123","aaa","@","@@","ali@veli"]
# sonuc =filter (lambda kelime :"@" in kelime,liste)
# print(*sonuc)

# verilen listedebütün harfleri büyük olanlar
# liste=["123","aaa","@","ali","VELI"]
# sonuc =filter (lambda kelime : kelime.isupper(),liste)
# print(*sonuc)

# müşteriler listesi müşteri no ile bakiye miktarı
# musteriler= [[1, 12], [2, 600], [ 3, 500], [4,150]]
# sonuc = filter(lambda x: (x[1] > 149),musteriler )
# print(*sonuc)

# müşteriler listesi (isim) müşteri no ile bakiye miktarı
# liste=[["kisi1",150],["kisi3",20],["kisi3",360],["kisi4",260]]
# sonuc =filter (lambda kisi : kisi[1]>50,liste)
# print(*sonuc)

# ePosta listesinde il arama
# ePosta=[["aa@a.com","Konya"],["123@b.com", "Ankara"],["c@c.net","İzmir"]]
# sonuc =filter (lambda sehir : sehir[1]=="Konya",ePosta)
# print(*sonuc)