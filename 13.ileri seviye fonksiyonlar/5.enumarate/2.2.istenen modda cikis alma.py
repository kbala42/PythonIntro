'''
---------------------------------------------------------tw:@tek_elo
listeyi enumerate ile indis atayıp içinden çift indislileri alıyoruz
--------------------------------------------------------------------
'''
liste = ["Konya","Yalova","Denizli","Van"]

for i,j in enumerate(liste):
    if (i%2==0):
        print(i,j)
