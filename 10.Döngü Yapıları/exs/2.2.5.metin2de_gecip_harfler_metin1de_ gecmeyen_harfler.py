"""
    Bir metinde geçen sesli harfler
"""
metin1="""Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği desktekeyen, 
platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."""
metin2=" Python interaktif yani etkileşimli bir programlama dilidir."

for i in metin2:
    if not i in metin1:
        print(i,end=",")
