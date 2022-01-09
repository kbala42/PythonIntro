kisi_bilgileri = {'ad':'ali','yas':40,'memleketi':'konya'}
print(kisi_bilgileri)

# deger değiştirme
kisi_bilgileri['yas'] =45
print(kisi_bilgileri)

# deger ekleme
kisi_bilgileri['adres'] = 'nişantaşı'
print(kisi_bilgileri)

# değer silme
kisi_bilgileri.pop("yas")
print(kisi_bilgileri)

# son öğeyi silmek için
kisi_bilgileri.popitem()
print(kisi_bilgileri)

# del (parametre) ile silme
del kisi_bilgileri["memleketi"]
print(kisi_bilgileri)

kisi_bilgileri = {'ad':'ali','yas':40,'memleketi':'konya'}
print(kisi_bilgileri)
kisi_bilgileri.clear()
print(kisi_bilgileri)

kisi_bilgileri = {'ad':'ali','yas':40,'memleketi':'konya'}
print(kisi_bilgileri)
del kisi_bilgileri
print(kisi_bilgileri)

