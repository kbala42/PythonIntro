print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringin ilk iki ve son iki elemaninindan yeni bir string oluşturan program 
      Örneğin;
      python -> pyon
      py -> pypy
      p -> None
      ''')
print('---------------------------------------------------------------------\n')

def strBasVeSonIkili(str):
    if len(str)<2:
        return 'None'
    else:
        return str[0:2]+str[-2: ]

print(strBasVeSonIkili('python'))
print(strBasVeSonIkili('py'))
print(strBasVeSonIkili('p'))

