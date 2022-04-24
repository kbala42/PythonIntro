'''
---------------------------------------------------------tw:@tek_elo
try-except buluğunu kullanarak listedeki yalnızca sayıları yazdırma
--------------------------------------------------------------------
'''

liste = ["mert", "Konya", "5a24a", "500", "kemal","123"]

for eleman in liste:

    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass