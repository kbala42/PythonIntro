#liste_string=["aa@a","123",["123@b", "k"],["c@c"],"asd","k@k"]
liste=["aa@a","123"]
sonuc_string=filter(lambda kelime:"@" in kelime, liste)
print(*sonuc_string)

Iiste=["123","aaa","@","@@","ali@veli"]
sonuc =filter (lambda kelime :"@" in kelime,liste)
print(*sonuc)

Iiste=["123","aaa","@","ali","VELI"]
sonuc =filter (lambda kelime : kelime.isupper(),liste)
print(*sonuc)

#müşteriler listesi müşteri no ile bakiye miktarı
musteriler= [[1, 12], [2, 600], [ 3, 500], [4,150]]
sonuc = filter(lambda x: (x[1] > 149),musteriler )
print(*sonuc)

liste=[["kişi1",150],["kişi3",20],["kişi3",360],["kişi4",260]]
sonuc =filter (lambda kişi : kişi[1]>50,liste)
print(*sonuc)