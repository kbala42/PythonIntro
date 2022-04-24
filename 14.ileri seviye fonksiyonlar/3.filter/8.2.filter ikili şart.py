'''
---------------------------------------------------------tw:@tek_elo
filter fonksiyonu ile iki de daha fazla şart uygulanabilir
--------------------------------------------------------------------
'''
liste=[["kişi1",150],["kişi2",20],["kişi3",360],["kişi4",260]]

# 50 den büyük 170 den küçük olanların listesi
sonuc =filter (lambda kişi : kişi[1]>50 and kişi[1]<170,liste)
print(*sonuc)

# 3 elamanlı alt listelerde çıkış
liste3=[["kişi1",150,10],["kişi2",65,3],["kişi3",360,12],["kişi4",260,10]]

# indis 1 de 50 den indis 2 de küçük olanların listesi
sonuc3 =filter (lambda kişi : kişi[1]>50 and kişi[2]<5,liste3)
print(*sonuc3)