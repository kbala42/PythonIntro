'''
---------------------------------------------------------tw:@tek_elo
Ekkulanım (overloading) kalıtılan sınıftaki methot temel sınıftaki
aynı adlı methottan farklı işlemler yaptırılmasına denir
--------------------------------------------------------------------
'''
# Temel sınıf
class Hayvan():

    def turunuYazdir(self):
        print("Hayvan türünde")
#Kalıtılan sınıf
class Penguen(Hayvan):
    # kalıtılan sınıfta ki methot farklı işleve sahip
    def turunuYazdir(self):
        print("Penguen türünde")

penguen=Penguen()
penguen.turunuYazdir()

