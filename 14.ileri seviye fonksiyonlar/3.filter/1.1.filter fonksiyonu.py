'''
---------------------------------------------------------tw:@tek_elo
filter(fonksiyon, liste) listede verilen değerleri fonksiyon sağlıyorsa
yeni bir dizi döndürür
--------------------------------------------------------------------
'''
# Diziye mod işlemi yaptığımızda, kalan 1 olanlarla yeni bir dizi oluşturuyor
sonuc=filter(lambda x:x%2,[1,2,3,4,5,6,7,8] )

# Dizinin tipi filter tipinde bir nesne
print(type(sonuc))

#sonuç filter sınııfından bir nesne, adresi
print(sonuc)

#sonucu yine * işaretçisi ile okunabilir
#print(*sonuc)

#sonuç dizisini döngü ile yazdırıyoruz
for s in sonuc:
    print(s)

