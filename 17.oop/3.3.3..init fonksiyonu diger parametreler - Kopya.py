'''
---------------------------------------------------------tw:@tek_elo
__init__ metodu birden fazla parametre alabilir
--------------------------------------------------------------------
'''
class Sinif:
    #init parametre olan değerlerin mutlaka sınıf örneği alınırken eklenmesi gerekir
    def __init__ (self,isim,soyisim,numara):
        print("merhaba",isim, soyisim, numara)

nesne=Sinif("mehmet","demir",46)


