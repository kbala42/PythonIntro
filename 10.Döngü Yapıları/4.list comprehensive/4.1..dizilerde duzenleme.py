print('----------------------------------------------------------tw:@tek_elo')
print('İç içe döngüler yada tek satır özelliği ile düzenleme yapılabilir')
print('---------------------------------------------------------------------')

liste=[[1,2,3,4],[5,6],[7,8,9,10,11,12]]

print('----------------------------')
print('İç içe düngülerle genişletme')
print('----------------------------')
for i in liste:
    for k in i:
        print (k)
print("--------------------------------------")
liste2=list()
for i in liste:
    for k in i:
        liste2.append(k)
print (liste2)
print()

print('----------------------------------------')
print('İç içe düngülerle genişletme - tek satır')
print('----------------------------------------')
liste3=[k for i in liste for k in i]
print (liste3)
print()

print('liste2:',id(liste2))
print('--------------------')
print('liste3:',id(liste3))
