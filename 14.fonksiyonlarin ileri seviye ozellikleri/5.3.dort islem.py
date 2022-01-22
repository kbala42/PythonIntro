'''
---------------------------------------------------------tw:@tek_elo
İç içe fonksiyonlarda iç içe birden fazla fonksiyon kullanılabilir
--------------------------------------------------------------------
'''
def islemYap(islemAdi):
    def topla(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carp(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islemAdi == "topla":
        return topla
    else:
        return carp

islem = islemYap("topla")
print(islem)
print(islem(1,2,3,4,5))

print("------------------------")

islem = islemYap("carp")
print(islem)
print(islem(1,2,3,4,5))

print("------------------------")

print(islemYap("carp")(1,2,3,4))

print("------------------------")

print(islemYap("topla")(1,2,3,4))