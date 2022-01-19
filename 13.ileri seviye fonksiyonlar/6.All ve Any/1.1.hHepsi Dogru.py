def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste=[True, False, True, False, False]

print(hepsi(liste))