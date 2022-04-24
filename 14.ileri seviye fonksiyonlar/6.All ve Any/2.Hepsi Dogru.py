'''
---------------------------------------------------------tw:@tek_elo
Listenin tümü True'mu? Sayısal değerler. İçinde değer döndürmeyen var mı?
--------------------------------------------------------------------
'''
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste=[4,-1,8,100]

print(hepsi(liste))