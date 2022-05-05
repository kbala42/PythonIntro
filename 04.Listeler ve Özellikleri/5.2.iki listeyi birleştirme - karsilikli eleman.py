print('-------------------------------------------------------------@tek_elo')
print('iki listenin elemanları karşılıklı birleştirilip\n'
      'yeni liste oluşturulabilir')
print('---------------------------------------------------------------------')
print()
listel=[1,2,3,4,5,6,7]
liste2=["python","java","c","c++","c#","pascal","cobol"]

altListeTuple=[]
altListeListe=[]

for i in range(len(listel)) :
    altListeTuple.append((listel[i],liste2[i]))
    altListeListe.append([listel[i],liste2[i]])

print(altListeTuple)
print(altListeListe)