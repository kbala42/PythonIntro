'''
---------------------------------------------------------tw:@tek_elo
1 ile 6 arasında ki sayılarını alarak bir listede saklayan program
--------------------------------------------------------------------
'''
def kareAl():
    sonuc = []
    for i in range(1,6):
        sonuc.append(i ** 2)
    return sonuc
print(kareAl())