'''
---------------------------------------------------------tw:@tek_elo
Liste içinde ki çift sayıları try-except ve raise kullanarak
yazdıran program
--------------------------------------------------------------------
'''
def ciftMi(sayi):
    if (sayi % 2 == 0):
        return sayi
    else:
        raise ValueError

liste = [500, 0, 15, 17, 2019, 2022]

for i in liste:
    try:
        print(ciftMi(i))
    except ValueError:
        pass