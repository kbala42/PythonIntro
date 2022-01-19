def davetiye_metni (isim):
    gonderilecek_metin ="Sayın "+isim+"\n"+" Bu mutlu günümüzde sizleri de aramızda görmekten mutluluk duyarız."
    return gonderilecek_metin

isimler=["Ali","Ayşe","Murat","Elif"]

for birey in isimler:
    print(davetiye_metni (birey))