print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringte en uzun kelimeyi ve uzunlugunu bulma 
      ''')
print('---------------------------------------------------------------------\n')

def enUzunKelime(dizi):
    kelimeVeUzunluklari = []
    for i in dizi:
        kelimeVeUzunluklari.append((len(i), i))
    kelimeVeUzunluklari.sort()
    return kelimeVeUzunluklari[-1][0], kelimeVeUzunluklari[-1][1]

kelime = enUzunKelime(['Ankara', 'İstanbul','İzmir','Bursa'])
print('En uzun kelime:', kelime[1])
print('En uzun kelime uzunluğu:', kelime[0])




