onMesaj="Sayın "
mesajSonu=" Mayıs 2020 dönemi faturanız: "
aboneNo="29101923"
tuketim=20
tuketimTutari=int(tuketim)*1.0
mesaj=onMesaj+str(aboneNo)+' nolu abonemiz ' + mesajSonu+str(tuketimTutari)+" TL' dir. Python Belediyesi"
print(mesaj)