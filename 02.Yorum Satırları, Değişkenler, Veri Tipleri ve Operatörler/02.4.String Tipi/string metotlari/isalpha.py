'''
-------------------------------------------------------------------tw:@tek_elo

    isalpha() metodu  stringin tamü harflerden oluşup oluşmadığını
                      kontrol eder.

                      Boşul ve özel karakterler yer alamaz

------------------------------------------------------------------------------
'''

txt1 = 'Merhaba'
print(txt1.isalpha())
print()

print('--------------------------------------')
print('Boşluk yer alamaz')
txt2 = 'Merhaba Dünya'
print(txt2.isalpha())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Özel karakter veya rakam yer alamaz')
txt3 = 'Merhaba5'
print(txt3.isalpha())
print('--------------------------------------')
print()