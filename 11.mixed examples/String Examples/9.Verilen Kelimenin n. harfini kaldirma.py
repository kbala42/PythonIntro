print('----------------------------------------------------------tw:@tek_elo')
print('''
      Verilen Kelimenin n. harfini kaldirma
      ''')
print('---------------------------------------------------------------------\n')

def harfKaldir(kelime, n):
    ilkParca = kelime[:n]
    sonParca = kelime[n+1:]
    return ilkParca+sonParca

print(harfKaldir('Merhaba', 3))





