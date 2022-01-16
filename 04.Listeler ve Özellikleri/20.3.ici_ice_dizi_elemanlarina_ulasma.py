print('-------------------------------------------------------------@tek_elo')
print('İç içe verilen dizilerin herbir elemanına ulaşma')
print('---------------------------------------------------------------------')
print()

liste=[[3,4] , [7,8], [10,11], [14,15]]

print('--------------------------')
print('Tek for kullanarak')
print('--------------------------')
for i,j in liste:
     print(i,j)
print()

print('--------------------------')
print('İç içe iki f0r  kullanarak')
print('--------------------------')
for i in liste:
    for j in i:
        print(j,end=" ")
    print()
