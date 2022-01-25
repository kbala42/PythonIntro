'''
---------------------------------------------------------tw:@tek_elo
init fonksiyonu ile nesne oluşturulan parametreyi direkt kullanabilir
--------------------------------------------------------------------
'''
class Kare:
    # 'kenar' parametresi ile init fonksiyonunu başlatıyoruz
    def __init__(self,kenar):
        #kenar parametresini nesne içinde kullanmak için
        # self.kenar atıyoruz
        self.kenar = kenar

    def alanHesapla(self):
        # self parametresi ile diğer metoda dahil ediyoruz
        # yeni tanımladığımız self.alan değişkeni ile sınıf içinde
        # fonksiyon dönüşü sağlıyoruz
        self.alan=self.kenar*self.kenar
        return self.alan
# kare nesnei oluştururken 5 değerini 'kenar' parametresi olarak alıyoruz
kare=Kare(5)
# 5 değeri ile alanHesapla metodunu çağırıyoruz
a=kare.alanHesapla()
print("Alan: ",a)

# kenar özelliği başlangıçtan sonra değiştirilebilir
kare.kenar=8
#yeni girilen değerle alanı hesaplatıyoruz
a=kare.alanHesapla()
print("Alan: ",a)


