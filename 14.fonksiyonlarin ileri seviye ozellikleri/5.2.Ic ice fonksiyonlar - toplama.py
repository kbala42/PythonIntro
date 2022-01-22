'''
---------------------------------------------------------tw:@tek_elo
İç içe fonksiyonlarda, fonksiyonlara ait bütün işlemler yapılabilir
--------------------------------------------------------------------
'''
def giris(*args):
    def topla(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(topla(args))

giris(1,2,3,4,5)
