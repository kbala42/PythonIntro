'''
---------------------------------------------------------tw:@tek_elo
**kwargs keyfi parametresi; kaç tane anahtar parametre olcağı
önceden belli değilse kullanılır
--------------------------------------------------------------------
'''
def ogrenci(**kwargs):
    print(kwargs)

ogrenci(ad="Hasan",soyad="Kara",sinif="10-Elk", numara=535)
