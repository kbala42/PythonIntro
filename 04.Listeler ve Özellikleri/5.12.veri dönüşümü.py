liste=[1,2,3,4,5,'ankara']
print(liste)
liste[0]=str("kocaeli")
liste[2]=float(1.5)
liste[5]=int(20)
print(liste)

meyve="elma"
print (meyve)
liste=list(meyve)
print (liste)

liste=list(range(1,15,2))
print(liste)
liste.sort()
print(liste)
liste.reverse()
print(liste)

cumle="23 nisan herkese mutlu olsun"
kelimeler=cumle.split(" ")
print("cümlenizde ",len(kelimeler),"adet kelime vardır")

bilgi=input("bilgilerinizi araya virgül koyarak yazınız: ")
liste=bilgi.split(",")
print(liste)