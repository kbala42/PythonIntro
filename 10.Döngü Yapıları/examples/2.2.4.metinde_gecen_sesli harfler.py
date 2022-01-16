"""
    Bir metinde geçen sesli harfler
"""
metin="""Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği desktekeyen, 
platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."""
sesli_harfler="aıioöuü"
sayac=0
for i in metin:
    if i in sesli_harfler:
        print(i,end=",")
