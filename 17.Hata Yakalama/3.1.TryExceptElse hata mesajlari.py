'''
---------------------------------------------------------tw:@tek_elo
else bir hata meydana gelmediyse yürütülecek kod bloğu
--------------------------------------------------------------------
'''
try:
    sayi = int(input("Birinci Sayı :"))
except ValueError: # önceliklikle tam sayı değer girilip girlmediğini test ediyoruz
    print("Sayı girmediniz")
else: # eğer sayı tam ise bu kez sıfır girilip girilmediğini test ediyoruz
    try:
        print(10/sayi)
    except ZeroDivisionError:
        print("Sayı sıfıra bölünemez")