isimler=["Ali","Ayşe","Murat","Elif"]

yeni_liste=map(lambda isim:"Sayın "+isim+"\n"+" Bu mutlu günümüzde sizleri de aramızda görmekten mutluluk duyarız.\n",isimler)

print(*yeni_liste)

