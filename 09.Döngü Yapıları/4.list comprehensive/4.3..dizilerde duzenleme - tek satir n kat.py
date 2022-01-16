print('----------------------------------------------------------tw:@tek_elo')
print('tek satır özelliği ile n kat alma')
print('---------------------------------------------------------------------')
liste=[[1,2,3,4],[5,6],[7,8,9,10,11,12]]

liste3=[k*3 for i in liste for k in i]

print (liste3)
print()

print('liste:',id(liste))
print('--------------------')
print('liste3:',id(liste3))
