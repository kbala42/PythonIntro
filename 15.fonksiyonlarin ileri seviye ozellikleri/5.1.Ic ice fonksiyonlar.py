'''
---------------------------------------------------------tw:@tek_elo
İç içe fonksiyonlar tanımlanabilir
--------------------------------------------------------------------
'''
def disFonksiyon():
    print("Dış fonksiyondayız...")
    def icFonksiyon():
        print("İç fonksiyon çalıştı.")
    icFonksiyon() # iç fonksiyonu dış fonksiyon içinden çağırıyoruz
    print("Dış fonksiyon bitti....")

disFonksiyon() # dış fonksiyonu çağırıyoruz
#icFonksiyon() # iç fonksiyonu direkt çağırmaya çalışırsak bu fonksiyonu tanımadığı için hata verir
