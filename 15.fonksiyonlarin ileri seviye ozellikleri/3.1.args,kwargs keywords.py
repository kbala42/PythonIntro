'''
---------------------------------------------------------tw:@tek_elo
*args ve **kwargs parametreleri bir arada kullanılabilir
--------------------------------------------------------------------
'''
def ogrenci(*args,**kwargs):
    print("Notlar:")
    for i in args:
        print(i)
    print("------------")
    for i,j in kwargs.items():
        print(i,":",j)

ogrenci(50,90,80,ad="Hasan",soyad="Kara",sinif="10-Elk", numara=535)
