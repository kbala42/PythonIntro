a=int(input("bir sayı giriniz"))
asal=0
for i in range (2,a):
    if a%i==0:
        asal+=1
if asal==0:
    print("girdiğiniz sayı asal")
else:
    print("girdiğiniz sayı asal değil")