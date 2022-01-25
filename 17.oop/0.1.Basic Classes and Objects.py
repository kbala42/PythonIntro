'''
---------------------------------------------------------tw:@tek_elo
Python'da herşey bir nesnedir. Sınıflarda bu nesneleri üretmemizi
sağlayan bir kalıp, bir proje şeklinde düşünebiliriz
--------------------------------------------------------------------
'''
# ASinifim adında bir sınıf üretiyoruz
class ASinifim:
    #attributes
    #behaviours
    pass

# BSinifim adında bir sınıf üretiyoruz
class BSinifim(object):
    #attributes
    #behaviours
    pass

# ASinifim tipi
print(type(ASinifim))
# ASinifim temel fonksiyonu
print(ASinifim)

# BSinifim tipi
print(type(BSinifim))
# BSinifim temel fonksiyonu
print(BSinifim)

print("---------------------------")

# Sınıflardan nesneler oluşturuyoruz
aNesnem=ASinifim()
bNesnem=BSinifim()

print("---------------------------")

print(type(aNesnem))
# oluşturduğumuz nesnenin bellek adresi
# nesne oluştuğu için bir bellek adresine sahiptir
print(aNesnem)

print(type(bNesnem))
# oluşturduğumuz nesnenin bellek adresi
# nesne oluştuğu için bir bellek adresine sahiptir
print(bNesnem)