"""
    For döngüsünde range kullanımı
"""
print("\n-------------------------------------------")
print("0  ile 9 arasında ki sayıların yazımı")
print(*range(10))

print("\n-------------------------------------------")
print("0  ile 9 arasında ki sayıların yazımı")
for i in range(10):
    print(i,end=" ")

print("\n-------------------------------------------")
print("4  ile 9 arasında ki sayıların yazımı")
for i in range(4,10):
    print(i,end=" ")

print("\n-------------------------------------------")
print("0  ile 9 arasında ki çift sayıların yazımı")
for i in range(0,10,2):
    print(i,end=" ")

print("\n-------------------------------------------")
print("0  ile 9 arasında ki tek sayıların yazımı")
for i in range(1,10,2):
    print(i,end=" ")

print("\n-------------------------------------------")
print("9  ile 0 arasında ki sayıların 9 hariç yazımı")
for i in range(9,0,-1):
    print(i,end=" ")

print("\n-------------------------------------------")
print("9  ile 0 arasında ki sayıların 0 dahil yazımı")
for i in range(9,-1,-1):
    print(i,end=" ")

print("\n-------------------------------------------")
print("9  ile 0 arasında ki çift sayıların yazımı")
for i in range(10,-1,-2):
    print(i,end=" ")

print("\n-------------------------------------------")
print("9  ile 0 arasında ki tek sayıların yazımı")
for i in range(9,-1,-2):
    print(i,end=" ")