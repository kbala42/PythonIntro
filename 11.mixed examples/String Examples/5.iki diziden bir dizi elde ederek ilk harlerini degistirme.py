print('----------------------------------------------------------tw:@tek_elo')
print('''
      İki diziden bri diz elde ederek ilk harlerini degistiren program 
      Örneğin;
      'merhaba','python' ->       
      ''')
print('---------------------------------------------------------------------\n')

def strDegistirBirlestir(x,y):
    yeniX = x[0] + y[1:]
    yeniY = y[0] + x[1:]
    yeniX1 = y[:2] + x[2:]
    yeniY1 = x[:2] + y[2:]
    #return yeniX+' '+yeniY
    return yeniX1+' '+yeniY1

print(strDegistirBirlestir('merhaba','python'))


