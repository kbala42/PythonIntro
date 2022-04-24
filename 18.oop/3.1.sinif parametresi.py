'''
---------------------------------------------------------tw:@tek_elo
sınıf içinden diğer bir sınıf parametre olarak çağrılabilir.
--------------------------------------------------------------------
'''
class A:
    def goster(self):
        print('a')
class B(A):
    def izle(self):
        self.goster()

nesne=B()
nesne.izle()
nesne.goster()
