"""
    istenen sayıda satır ve sütün oluşturan programlar matris
"""
print("\n-------------------------------------------")
print("---5x5 matris * matris oluşturan program---")
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

print("---5x5 matrisini aütun sayıları le oluşturan program---")
for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()

print("---5x5 matrisini satır ve aütun sayıları le oluşturan program---")
for i in range(1,6):
    for j in range(1,6):
        print("({},{})".format(i,j),end="  ")
    print()

