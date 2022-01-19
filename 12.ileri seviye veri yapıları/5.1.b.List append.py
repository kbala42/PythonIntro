liste1=[1,2,3,4,5]
liste2=[]
liste3=[]
print(liste2)
for i in liste1:
    liste2.append(i)
print(liste2)
liste3=[i for i in liste1]
print(liste3)
liste4=[i**2 for i in liste1]
print(liste4)