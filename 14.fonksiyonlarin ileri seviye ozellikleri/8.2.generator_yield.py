'''
---------------------------------------------------------tw:@tek_elo
Generator tek tek sıralı olarak çağrılması gereken yerlerde kullanılır.
iterator bazı zorluklarını önlemek için kullanılmaktadır. Yine __next__()
ve__iter__() metotları kullanılır. return yerine yield ifadesi kullanılabilir.
Birden fazla yield kullanılabilir
------
'''
def kareAl():
    for i in range(1,6):
        yield i ** 2

generator = kareAl()

#tipi
print(type(generator))

#hafıza adresi
print(generator)

#içerik
print(*generator)
