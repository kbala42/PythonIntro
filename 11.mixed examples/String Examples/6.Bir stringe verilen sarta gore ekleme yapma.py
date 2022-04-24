print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringte sarta gore duzenleme yapma  
      Örneğin;
      Eğer 'not' izleyen 'poor' varsa 'good'
      Örnekler:
      'The lyrics is not that poor!' -> 'The lyrics is good!'
      'The lyrics is poor!' -> 'The lyrics is poor!'  
      ''')
print('---------------------------------------------------------------------\n')

def strNotPoor(metin):
    izlenen = metin.find('not')
    takipci = metin.find('poor')
    if takipci > izlenen and izlenen>0 and takipci>0:
        metin = metin.replace(metin[izlenen:(takipci+4)],'good')
        return metin
    else:
        return metin

print(strNotPoor('The lyrics is not that poor!'))
print()
print(strNotPoor('The lyrics is poor!'))



