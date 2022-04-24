print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringe verilen sarta gore ekleme yapma  
      Örneğin;
      ali -> aliler (3 ve daha fazla ise ler ekleyin)
      aliler -> alilerle (Eğer ler varsa sonuna le ekleyin)    
      a-> a (İkiden azsa olduğu gibi bırakın)
      al -> al  (İkiden azsa olduğu gibi bırakın)
      ''')
print('---------------------------------------------------------------------\n')

def strEkle(str):
    kacHarfli = len(str)
    if kacHarfli < 3:
        return str
    else:
        if str[-3:] != 'ler':
            return str +'ler'
        else:
            return str + 'le'

print(strEkle('ali'))
print()
print(strEkle('aliler'))
print()
print(strEkle('a'))
print()
print(strEkle('al'))


