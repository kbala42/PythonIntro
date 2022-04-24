'''
---------------------------------------------------------tw:@tek_elo
Verilen dizide bütün harfleri büyük olanları ayıran program
--------------------------------------------------------------------
'''
# 50 ye kadar olan sayılarla liste oluşturuyoruz
liste=[i*3 for i in range(50)]

#liste içinde ki elemanlardan 50 den büyük olanlarla sonuc filter nesnesi oluşturuyoruz
sonuc=filter(lambda x:x>50, liste)

# sonuc nesnesinin hafıza adresi
print(sonuc)

# sonuc nesnesini yazdırıyoruz
print(*sonuc)


