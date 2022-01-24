'''
---------------------------------------------------------tw:@tek_elo
try bloktaki kodda bir hata olup olmadığını test etmemizi sağlar
except hata olması durumunda yürütülecek blok
--------------------------------------------------------------------
'''
try: # Kullanıcıdan giriş yapmasını istiyoruz
    sayiBir = float(input("Birinci Sayı :"))
    sayiIki = int(input("İkinci Sayı :"))
except ValueError: # girilen değer yoksa yada tam sayı dışında (noktalı veya string) bir giriş yapılmışsa
    print("Sayı girmediniz. Lütfen girişi doğru giriniz:") # mesajı yazdırıyoruz
print("Giriş testi sona erdi...") # uyarı mesajından sonra program buradan devam ediyor