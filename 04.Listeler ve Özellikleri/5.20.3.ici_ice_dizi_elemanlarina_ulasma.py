"""
    İç içe verilen dizilerin herbir elemanına ulaşma
"""
liste=[[3,4] , [7,8], [10,11], [14,15]]

for i,j in liste:
     print(i,j)

for i in liste:
    for j in i:
        print(j,end=" ")
    print()
