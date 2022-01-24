'''
---------------------------------------------------------tw:@tek_elo
while ile hata tutucuları kullanılarak doğru bir sayının
girilmesi sağnabilir
--------------------------------------------------------------------
'''
while True:
    x = input("Bir sayı girin: ")
    if x=='q':
        break
    try:
        y = 1/float(x)
    except ValueError:
        print("Geçersiz sayı")
        continue
    except ZeroDivisionError:
        print("Sıfıra bölme hatası")
        continue
    print(y)