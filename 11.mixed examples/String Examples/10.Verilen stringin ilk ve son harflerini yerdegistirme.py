print('----------------------------------------------------------tw:@tek_elo')
print('''
      Verilen stringin ilk ve son harflerini yerdegistirme
      ''')
print('---------------------------------------------------------------------\n')

def ilkVeSonHarfiDegistir(kelime):
    ilkHarf = kelime[0]
    sonHarf = kelime[-1]
    kelimeKirp = kelime[1:-1]
    return sonHarf + kelimeKirp + ilkHarf

print(ilkVeSonHarfiDegistir('makas'))





