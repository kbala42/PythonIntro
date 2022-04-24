'''
---------------------------------------------------------tw:@tek_elo
Verilen dizide çift olanları yazdıran program
--------------------------------------------------------------------
'''
# 50 ye kadar olan sayılarla liste oluşturuyoruz
liste=[i*3 for i in range(50)]

#liste içinde ki elemanlardan çift olanlarla sonuc filter nesnesi oluşturuyoruz
sonuc=filter(lambda x:x%2==0, liste)

# sonuc nesnesini yazdırıyoruz
print("Çift olanlar: ", *sonuc)


