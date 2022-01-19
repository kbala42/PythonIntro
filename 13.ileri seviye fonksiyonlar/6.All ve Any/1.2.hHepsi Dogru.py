def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste=[4,-1,8,100]

print(hepsi(liste))