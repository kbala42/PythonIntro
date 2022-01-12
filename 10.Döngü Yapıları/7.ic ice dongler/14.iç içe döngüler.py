dersler = ["Ders 1", "Ders 2", "Ders 3"]
konular = ["Konu 1", "Konu 2", "Konu 3"]
for x in dersler:
    for y in konular:
        print(x, y)

i=1
while i<4:
    j=1
    while j<4:
        print("i nin değeri: {} j nin değeri: {} ".format(i,j))
        j=j+1
    i=i+1