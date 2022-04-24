print('----------------------------------------------------------tw:@tek_elo')
print('''
      13.Girilen metnin buyuk ve kucuk harf cikislarini gosteren program
      ''')
print('---------------------------------------------------------------------\n')

def metniBuyukVeKucukHarfeCevir(str):
    kucukHarf = str.lower()
    buyukHarf = str.upper()
    return kucukHarf, buyukHarf

metin = ''' 
    NumPy, Python programlama dili için büyük, çok boyutlu dizileri ve matrisleri destekleyen, 
    bu diziler üzerinde çalışacak üst düzey matematiksel işlevler ekleyen bir kitaplıktır.
'''
print('Küçük Harf:',metniBuyukVeKucukHarfeCevir(metin)[0])
print('Büyük Harf:',metniBuyukVeKucukHarfeCevir(metin)[1])
print('''
     Basit çözüm
''')

print('Küçük Harf:',metin.lower())
print('Büyük Harf:',metin.upper())





