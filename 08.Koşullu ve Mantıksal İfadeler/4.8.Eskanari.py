a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
if(a!=b and a!=c and b!=c):
    print("Çeşitkenar Üçgen!")
elif(a==b==c):
    print("Eşkenar Üçgen!")
else: print("İkizkenar Üçgen")