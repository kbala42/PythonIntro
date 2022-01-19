'''
---------------------------------------------------------tw:@tek_elo
print('faktöryel bulma dosyası için modül dosyası
--------------------------------------------------------------------
'''
def faktoryelAl(sayi):
    """
        Faktöryel Alma Modülü
    """
    faktoryel=1
    if (sayi == 0 or sayi==1):
        return 1
    else:
        while (sayi >= 1):
            faktoryel *= sayi
            sayi -= 1
        return faktoryel