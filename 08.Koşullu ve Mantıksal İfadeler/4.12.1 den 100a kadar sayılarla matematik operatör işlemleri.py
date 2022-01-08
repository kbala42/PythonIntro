"""
    1 den 10ea kadar sayılarla matematik işlemleri
"""
print("\n-------------------------------------------")
print("---0  ile 10 arasında ki sayıların toplamını bulan program---")
toplam=0
for i in range(10):
    toplam+=i
print("0  ile 100 arasında ki sayıların toplamı: ", toplam)
######################################################################
print("\n-------------------------------------------")
print("---10 satırlı sola yaslı dik üçgen çizem program---")
a=10
for i in range(1,11):
    print(i * "*")
    # print((2*i-1)*"*") ikinci çözüm
######################################################################
print("\n-------------------------------------------")
print("---10 satırlı saga yaslı dik üçgen çizem program---")
b=10
for i in range(1,11):
    print(b*" ",i*"*")
    b-=1
######################################################################
print("\n-------------------------------------------")
print("---10 satırlı eşkenar üçgen çizem program---")
b=10
for i in range(1,11):
    print(b*" ",(2*i-1)*"*")
    b-=1
######################################################################
print("\n-------------------------------------------")
print("---10 satırlı ters eşkenar üçgen çizem program---")
b=1
for i in range(10,0,-1):
    print(b*" ",(2*i-1)*"*")
    b+=1


"""
print("\n-------------------------------------------")
print("---2  ile 10 arasında ki asal sayıları bulan program--")
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            continue
    print("{} sayısı asaldır".format(i))
"""


