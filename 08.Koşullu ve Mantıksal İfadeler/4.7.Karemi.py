a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
d=int(input("4. kenar:"))
if(a==b==c==d):
    print("Kare!")
elif(a==c and b==d or a==b and c==d ):
    print("Dikdörtgen")
else: print("Diğer Dörtgen")