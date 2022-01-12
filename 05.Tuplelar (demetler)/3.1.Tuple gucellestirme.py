print('----------------------------------------------------------------tw:@tek_elo')
print('Tuple\'ları her ne kadar direkt değiştiremezsekte\n'
      'önce listeye çevirip günceleştirme yada ekleme yaptıktan sonra\n'
      'Tuple\'a tekrar dönüştürürüz')
print('---------------------------------------------------------------------------')
haftaninGunleri=("Pazartesi","Sali","Çrş","Perşembe","Cuma")

print(type(haftaninGunleri))
print(haftaninGunleri)
print()

print('---------------------------------')
print('Önce tuple\'ı listeye çeviriyoruz')
print('---------------------------------')
gunlerListe = list(haftaninGunleri)

print(type(gunlerListe))
print(gunlerListe)
print()

print('---------------------------------')
print('Listeye ekleme yapıyoruz')
print('---------------------------------')
gunlerListe.append('Cumartesi')
print('---------------------------------')
print('Listede düzenleme yapıyoruz')
print('---------------------------------')
gunlerListe[2]='Çarşamba'

print(gunlerListe)
print()

print('-----------------------------------')
print('Tekrar listeyi tuple\'a çeviriyoruz')
print('-----------------------------------')

haftaninGunleri=tuple(gunlerListe)

print(type(haftaninGunleri))
print(haftaninGunleri)
print()

print('----------------------------------------------------------')
print('Tuple\'da direkt yeni bir tuple eklemesi yapıp\n'
      ' aynı tuple\'ı yaptığımızda\n buna izin verir ')
print('----------------------------------------------------------')
x = ('Pazar',) # tek tuple ürettik
haftaninGunleri += x

print(type(haftaninGunleri))
print(haftaninGunleri)