sozluk = {'renk': 'mavi', 'kıyafet': 'pantolon', 'beden': 'M'}
for anahtar in sozluk:
    print(anahtar,sozluk[anahtar])
sozlukBilesenleri=sozluk.items()
print(sozlukBilesenleri)
for bilesen in sozlukBilesenleri :
    print(bilesen)
    print(type(bilesen))