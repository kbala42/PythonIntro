ic_ice_demet=((1,7),(1,9),(5,8,3),(4,3))
print(ic_ice_demet[2])
print(ic_ice_demet[2][1])
print("-------Döngü ile dış demet elemanlarına ulaşma---------------")
for i in ic_ice_demet:
    print(i)
print("------Döngü ile bütün elemanlara ulaşma------------------------")
for i in ic_ice_demet:
    for j in i:
        print(j,end=" ")
    print()
