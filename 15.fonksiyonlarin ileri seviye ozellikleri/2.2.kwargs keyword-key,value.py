'''
---------------------------------------------------------tw:@tek_elo
**kwargs ın anhtar ve değerleri ayrı ayrı alınabilir
--------------------------------------------------------------------
'''
def ogrenci(**kwargs):
    for i,j in kwargs.items():
        print("Key:",i,"Value:",j)

ogrenci(ad="Hasan",soyad="Kara",sinif="10-Elk", numara=535)
