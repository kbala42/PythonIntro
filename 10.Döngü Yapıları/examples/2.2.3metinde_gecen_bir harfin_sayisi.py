"""
    Bir metinde genen bir harfin sayısı
"""
metin="""Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği desktekeyen, 
platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."""
harf="a"
sayac=0
for i in metin:
    if i == harf:
        sayac +=1
#print("metinde ki {} harf sayısı {} ", format(harf, str(sayac)))
print(sayac)