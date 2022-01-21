'''
---------------------------------------------------------tw:@tek_elo
filter fonksiyonu cevap anahtarı ile
öğrencinin verdiği cevapları karşılaştırma
--------------------------------------------------------------------
'''

cevapAnahtarı=["a","c","e","b","a"]
ogrenci=["a","d","d","b","a"]

# Öğrencinin verdiği cevaplarla cevap anatarını karşılaştırıyoruz
# Sonuç doğru ise doğru
# Sonuç yanlış ise yanlış
# olan liste hazırlıyoruz
liste=list(map(lambda x,y: "doğru" if x==y else "yanlış",cevapAnahtarı,ogrenci))

# listeyi yazdırıyoruz
print(liste)
