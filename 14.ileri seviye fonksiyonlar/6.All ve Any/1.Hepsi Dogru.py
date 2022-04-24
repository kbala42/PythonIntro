'''
---------------------------------------------------------tw:@tek_elo
Listenin tümü True'mu? Mantıksal değerler
--------------------------------------------------------------------
'''
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste=[True, False, True, False, False]

print(hepsi(liste))