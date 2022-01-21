'''
---------------------------------------------------------tw:@tek_elo
iki sözlüğe zip fonksiyonu uygulamak
--------------------------------------------------------------------
'''
sozluk1={"Bir":1,"İki":2,"Uc":3}
sozluk2={"Marmara":"Bursa", "İçAnadolu":"Konya","Akdeniz":"Antalya"}

listAnahtar=list(zip(sozluk1,sozluk2))
print(listAnahtar)

listDeger=list(zip(sozluk1.values(),sozluk2.values()))
print(listDeger)
