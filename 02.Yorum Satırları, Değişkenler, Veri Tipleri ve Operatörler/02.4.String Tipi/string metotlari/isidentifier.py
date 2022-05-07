'''
-------------------------------------------------------------------tw:@tek_elo

    isidendifier() metodu   geçerli bir tanıcı olup olmadığını belirtir
                            (a,z) büyük ve küçük harf yazılabilir. Özel karakterler olmaz
                            (0,9) rakam blunabilir ama başlayamaz
                            boşluk yer alamaz
                            (_) alt çizgi ile başlayabilir

------------------------------------------------------------------------------
'''

txt1 = 'sayi'
print(txt1.isidentifier())
print()

print('--------------------------------------')
print('Sayı ile başlayamaz')
txt2 = '1sayi'
print(txt2.isidentifier())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Boşluk olamaz')
txt3 = 'sayi 1'
print(txt3.isidentifier())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Özel karakter * olamaz')
txt4 = 'sayı*'
print(txt4.isidentifier())
print()

print('----------------------------------------')
print('Alt çizgi ile başlayabilir')
txt5 = '_sayi'
print(txt5.isidentifier())
print('----------------------------------------')
print()


