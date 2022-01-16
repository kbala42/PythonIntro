print('----------------------------------------------------------tw:@tek_elo')
print('100 e kadar olan sayıları ekrana yazdıran program')
print('---------------------------------------------------------------------')
print()
print('---------------------------------------------------------------------')
print('1. çözümde her sayıyı mod işlemine tabi tutuyoruz\n')
print('Eğer sonuç sıfırsa yani tam bölünüyorsa yazdırıyoruz')
print('---------------------------------------------------------------------')
a=1
while a<=100:
    if a%2==0:
        print(a,end=",")
    a+=1
print()

print('---------------------------------------------------------------------')
print('2 den sonra ki sayıları 2 arttırarak buluyoruz')
print('---------------------------------------------------------------------')
a=2
while a<=100:
    print(a,end=",")
    a+=2



