liste=[["kişi1",150],["kişi2",20],["kişi3",360],["kişi4",260]]
#sonuc =filter (lambda kişi : kişi[1]>50,liste)
sonuc =filter (lambda kişi : kişi[1]>50 and kişi[1]<170,liste)
print(*sonuc)

liste3=[["kişi1",150,10],["kişi2",65,3],["kişi3",360,12],["kişi4",260,10]]
sonuc3 =filter (lambda kişi : kişi[1]>50 and kişi[2]<5,liste3)
print(*sonuc3)