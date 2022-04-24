'''
---------------------------------------------------------tw:@tek_elo
iterator yinelenebilir nesneler (liste, tuple, set ve dictionary)
arasında gezinti yapılabilmesine olanak tanıyan yapılardır
--------------------------------------------------------------------
'''
liste = [1,2,3,4,5]

# listeyi iterator listeye dönüştürüyoruz
iterator = iter(liste)

print(type(iterator))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) # Eleman sayısını geçtiği zaman hata veir

listeSehir = ['Konya', 'Yalova', 'İstanbul']

# listeyi iterator listeye dönüştürüyoruz
iteratorSehir = iter(listeSehir)

print(next(iteratorSehir))
print(next(iteratorSehir))
print(next(iteratorSehir))

kelime = 'Merhaba'

iterKelime = iter(kelime)

print(next(iterKelime))
print(next(iterKelime))
print(next(iterKelime))
print(next(iterKelime))
print(next(iterKelime))
print(next(iterKelime))
print(next(iterKelime))