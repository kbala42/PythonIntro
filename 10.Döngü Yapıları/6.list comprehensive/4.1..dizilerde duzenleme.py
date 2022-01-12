liste=[[1,2,3,4],[5,6],[7,8,9,10,11,12]]

for i in liste:
    for k in i:
        print (k)
print("--------------------------------------")
liste2=list()
for i in liste:
    for k in i:
        liste2.append(k)

print (liste2)
print("--------------------------------------")
liste3=[k for i in liste for k in i]

print (liste3)


