liste=[5,9,7,1,2,3,6,4]
buyuk=0
kucuk=999
for i in range(len(liste)):
    if liste[i]>buyuk:
        buyuk=liste[i]
    if liste[i]<kucuk:
        kucuk=liste[i]
print("""girilen sayıların en büyüğü= {} girilen sayıların en küçüğü= {}""".format(buyuk,kucuk))