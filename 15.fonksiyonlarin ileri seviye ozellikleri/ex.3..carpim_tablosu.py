'''
---------------------------------------------------------tw:@tek_elo
Generator kullanarak çarpım tablosunun hazırlanması
-------------------------------------------------------------------
'''
def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)
for i in carpimTablosu():
    print(i)