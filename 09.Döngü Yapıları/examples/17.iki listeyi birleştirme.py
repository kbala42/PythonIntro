print('''
-----------------------------------------------------------------------------tw:@tek_elo
iki listeyi birleştirme - liste ve tuple
----------------------------------------------------------------------------------------''')
liste1=[1,2,3,4,5,6,7]
liste2=["python","java","c","c++","c#","pascal","cobol"]
listeYeni=[]
listeTuple=[]
for i in range(len(liste1)):
    listeYeni.append([liste1[i],liste2[i]])
    listeTuple.append((liste1[i], liste2[i]))
print(listeYeni)
print(listeTuple)