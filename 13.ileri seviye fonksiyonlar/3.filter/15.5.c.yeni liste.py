"""
Elinizde bir teste ait cevap anahtarı ve öğrenci cevaplarının olduğu listeler var. siz bu cevapları
anahtar ile kontrol ederek sonuçları doğru veya yanlış olarak çıktı almak istiyorsunuz. Bunu yapacak
kodları lambda ve map fonksiyonları ile nasıl yaparsınız.
Örnek: cevap_anahtarı=[“a”,“c”,“e”,“b”,“a”] ogrenci_1=[“a”,“d”,“d”,“b”,“a”]
"""
cevapAnahtarı=["a","c","e","b","a"]
ogrenciBir=["a","d","d","b","a"]

liste=list(map(lambda x,y: "doğru" if x==y else "yanlış",cevapAnahtarı,ogrenciBir))

print(liste)
