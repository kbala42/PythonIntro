sebzeler =["lahana","marul","pırasa","ıspanak"]
print(sebzeler)
sebzeler.append("fasulye")
print(sebzeler)
sebzeler.insert(2,"patlıcan")
print(sebzeler)
sebzeler2=sebzeler.copy()
print(sebzeler2)
print(sebzeler.count("marul"))
sebzeEkle=["biber","domates"]
sebzeler.extend(sebzeEkle)
print(sebzeler)

print(sebzeler.index("ıspanak"))

print(sebzeler2)
sebzeler2.clear()
print(sebzeler2)

print(sebzeler)
sebzeler.pop(4)
print(sebzeler)

print(sebzeler)
sebzeler.remove('fasulye')
print(sebzeler)

print(sebzeler)
sebzeler.reverse()
print(sebzeler)

print(sebzeler)
sebzeler.sort()
print(sebzeler)

print(sebzeler)
del sebzeler[3]
print(sebzeler)

print(len(sebzeler))
