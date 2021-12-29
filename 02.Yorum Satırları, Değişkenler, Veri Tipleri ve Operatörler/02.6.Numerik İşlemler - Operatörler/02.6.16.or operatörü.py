sayi1=5
#or operatörü kullanımı
print (sayi1<6 or sayi1>10)
adi='Elif'
print (adi=='Elif' or adi=='Emre')
#Adı Elif veya Emre ise True değerini döndürür.
meslekUnvani='Mühendis'
meslek='Mimar'
print (meslekUnvani=='Öğretmen' or meslek=='Doktor')
#Meslek ünvanı Öğretmen veya Doktor olmadığı için False döndürür.
print (meslekUnvani=='Öğretmen' or meslekUnvani=='Doktor' or
meslekUnvani=='Mühendis')
#Meslek Ünvanı Öğretmen veya Doktor veya Mühendis'ten biri ise True değerinidöndürür.
# İkiden fazla koşul için de kullanılabilir.