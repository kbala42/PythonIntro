'''
---------------------------------------------------------tw:@tek_elo
Nesneye ait fonksiyonlara özel olarak metot ismi verilir.
self parametesi sınıfa ait değişkenlere sınıf içinden ulaşmak için kullanılır
--------------------------------------------------------------------
'''
# Kare sınıfı oluşturuyoruz
class Kare:
    kenar=5
    # sınıfa ait metot oluşturuyoruz
    def alanHesapla(self):
        # sınıf özelliğine alarak işlem yapıyoruz
        alan=self.kenar*self.kenar
        print("Alan:",alan)
#kare nesnemizi üretiyoruz
kare=Kare()
#alanHesapla metodunu çağırıyoruz
kare.alanHesapla()

