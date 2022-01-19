def davetiye_metni (isim):
    gonderilecek_metin ="Sayın "+isim+"\n"+" Bu mutlu günümüzde sizleri de aramızda görmekten mutluluk duyarız.\n"
    return gonderilecek_metin

isimler=["Ali","Ayşe","Murat","Elif"]

davetiye =map(davetiye_metni, isimler)
print(davetiye) #davetiye değişkeninin bellek adresini yazdırır
print(*davetiye) #davetiye değişkeninin değerini yazdırır