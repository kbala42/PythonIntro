print('----------------------------------------------------------tw:@tek_elo')
print('''
      Verilen stringin indisi tek olan harfleri kaldirma
      ''')
print('---------------------------------------------------------------------\n')

def indisTekseKaldir(kelime):
    sonuc = ''
    for i in range(len(kelime)):
        if i % 2 == 0:
            sonuc += kelime[i]
    return sonuc

print(indisTekseKaldir('istanbul'))





