print('''
-----------------------------------------------------------------------------tw:@tek_elo
Kullanıcıdan satır ve sütun sayısı değerlerini alarak\n
sayıları tablo şeklinde yazan program
----------------------------------------------------------------------------------------''')
a=int(input('tablonun satır uzunluğunu giriniz:'))
b=int(input('tablonun sütun uzunluğu giriniz:'))
for i in range(1,a+1):
    for j in range(1,b+1):
        print(j,end=" ")
    print( )