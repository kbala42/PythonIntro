'''
-------------------------------------------------------------------tw:@tek_elo

    isalnum() metodu  stringin sayı, harflerden oluşup oluşmadığını
                      kontrol eder.

                      Boşul ve özel karakterler yer alamaz

------------------------------------------------------------------------------
'''

txt = 'Merhaba'
print(txt.isalnum())
print()

txt1 = 'Merhaba5'
print(txt1.isalnum())
print()

print('--------------------------------------')
print('Boşluk yer alamaz')
txt2 = 'Sayi 5'
print(txt2.isalnum())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Özel karakter veya rakam yer alamaz')
txt3 = 'Sayi5.'
print(txt3.isalnum())
print('--------------------------------------')
print()