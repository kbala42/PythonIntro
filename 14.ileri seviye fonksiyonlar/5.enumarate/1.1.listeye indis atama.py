'''
---------------------------------------------------------tw:@tek_elo
bir listeye indis atama işlemi
--------------------------------------------------------------------
'''
liste = ["Konya","Yalova","Denizli","Van"]

i=0
sonuc=list()

while (i<len(liste)):
    sonuc.append((i,liste[i]))

    i+=1

print(sonuc)
