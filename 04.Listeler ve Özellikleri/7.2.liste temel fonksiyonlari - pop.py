print('-------------------------------------------------------------@tek_elo')
print('liste temel metotları')
print('---------------------------------------------------------------------')
print()

sebzeler =["lahana","marul","pırasa","ıspanak"]
print(sebzeler)
print()

sebzeler.append("fasulye")
print(sebzeler)
print()

sebzeler.insert(2,"patlıcan")
print(sebzeler)
print()

sebzeler2=sebzeler.copy()
print(sebzeler2)
print()

print(sebzeler.count("marul"))
sebzeEkle=["biber","domates"]
sebzeler.extend(sebzeEkle)
print(sebzeler)
print()

print(sebzeler.index("ıspanak"))

print(sebzeler2)
sebzeler2.clear()
print(sebzeler2)
print()

print(sebzeler)
sebzeler.pop(4)
print(sebzeler)
print()

print(sebzeler)
sebzeler.remove('fasulye')
print(sebzeler)
print()

print(sebzeler)
sebzeler.reverse()
print(sebzeler)
print()
print()

print(sebzeler)
sebzeler.sort()
print(sebzeler)
print()

print(sebzeler)
del sebzeler[3]
print(sebzeler)
print()

print(len(sebzeler))
