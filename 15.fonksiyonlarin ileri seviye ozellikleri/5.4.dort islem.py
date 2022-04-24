'''
---------------------------------------------------------tw:@tek_elo
İç içe fonksiyonları önce ayrı fonksiyon şeklinde
daha sonra diğer fonksiyonun içersinde kullanılabilir
--------------------------------------------------------------------
'''
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islemYap(f1, f2, f3, f4, islemAdi):
    if islemAdi == "toplama":
        print(f1(1,2))
    elif islemAdi == "cikarma":
        print(f2(5,3))
    elif islemAdi == "carpma":
        print(f3(2,3))
    elif islemAdi == "bolme":
        print(f4(6,3))
    else:
        print("Geçesiz işlem !")

islemYap(toplama,cikarma,carpma,bolme,"carpma")

print("--------------------")

islemYap(toplama,cikarma,carpma,bolme,"bolme")