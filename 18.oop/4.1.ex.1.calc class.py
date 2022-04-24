'''
---------------------------------------------------------tw:@tek_elo
Hesap makinesi sınıfı
--------------------------------------------------------------------
'''
class Calc(object):
    # a ve b parametreleri sınıfı tanımlıyoruz
    def __init__(self, a, b):

        #sınıf parametrelerini tanımlıyoruz
        self.value1=a
        self.value2=b

    def add(self):
        # add metodu çağrıldığında sınıf parametrelerinin toplamını döndürüyoruz
        return self.value1 + self.value2

    def subtract(self):
        # subtract metodu çağrıldığında sınıf parametrelerinin farkını döndürüyoruz
        return self.value1 - self.value2

    def multiply(self):
        # multiply metodu çağrıldığında sınıf parametrelerinin çarpımını döndürüyoruz
        return self.value1 * self.value2

    def division(self):
        # division metodu çağrıldığında sınıf parametrelerinin bölümünü döndürüyoruz
        return self.value1 / self.value2

a=20
b=10

# a veb parametreleri ile calc nesnesini üretiyoruz
calc=Calc(a,b)

print("{} + {} = {}".format(a,b,calc.add())) # add metodunu çağırıyoruz
print("{} - {} = {}".format(a,b,calc.subtract())) # subtract metodunu çağırıyoruz
print("{} x {} = {}".format(a,b,calc.multiply())) # multiply metodunu çağırıyoruz
print("{} / {} = {}".format(a,b,calc.division())) # division metodunu çağırıyoruz