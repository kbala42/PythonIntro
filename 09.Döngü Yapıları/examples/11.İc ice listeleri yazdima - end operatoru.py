print('''
-----------------------------------------------------------------------------tw:@tek_elo
İç içe listeleri yazdırma; end operatörü kullanarak
----------------------------------------------------------------------------------------''')
liste = [[3,4],[7,8],[10,11],[14,15]]
for i in liste:
    print(i,end=",")
print("\n*************")
for i,j in liste:
    print(i,end=",")
    print(j,end=",")
print("\n*************")
for i in liste:
    for j in i:
        print(j,end=",")