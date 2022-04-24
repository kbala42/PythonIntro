print('----------------------------------------------------------tw:@tek_elo')
print('''
      Bir stringin ilk ikarakterinin tekrarlarini gizleyen program 
      Örneğin;
      elimine etmek -> elimin* *tm*k     
      ''')
print('---------------------------------------------------------------------\n')

def strIlkHarfGizleme(str):
    ilkHarf = str[0]
    str = str.replace(ilkHarf, '*')
    str = ilkHarf+str[1:]
    return str

print(strIlkHarfGizleme('elimine etmek'))


