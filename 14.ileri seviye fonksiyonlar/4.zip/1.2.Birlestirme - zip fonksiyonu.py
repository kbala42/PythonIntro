'''
---------------------------------------------------------tw:@tek_elo
zip fonksiyonu parametre olarak verile listelerden yeni bir liste
döndürür. Ama dönen liste tuple cinsindendir
--------------------------------------------------------------------
'''
liste1=[3,9,2,5]
liste2=[8,21,50,5,1,7,4,]

#sonuc ortak indise sahip olan elemanlarla oluşturuluyor
sonuc=zip(liste1,liste2)
print(type(sonuc))
print(*sonuc)


