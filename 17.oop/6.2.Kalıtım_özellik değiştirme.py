'''
---------------------------------------------------------tw:@tek_elo
kalıttığımız sınıfın özelliğini değiştirebiliriz.
--------------------------------------------------------------------
'''
class A:
    def __init__(self, i=100):
        self.i = i
class B(A):
    def __init__(self, j=10):
        self.j = j

a=A()
# nesnenin özelliği i
print(a.__dir__())
b=B()
# kalıtılan nesnenin özelliğinde artık j var
print(b.__dir__())