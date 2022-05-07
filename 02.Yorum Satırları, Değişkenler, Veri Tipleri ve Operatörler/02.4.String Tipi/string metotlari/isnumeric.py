'''
-------------------------------------------------------------------tw:@tek_elo

    isnumeric() metodu  stringin (0-9) arasındaki rakamlardan oluşup oluşmadığını
                        kontrol eder.

------------------------------------------------------------------------------
'''

txt1 = '12300'
print(txt1.isnumeric())
print()

print('--------------------------------------')
txt2 = '0012300'
print(txt2.isnumeric())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Eksi sayılar numerik olarak düşünülmez')
txt3 = '-12'
print(txt3.isnumeric())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Noktalı sayılar numerik olarak düşünülmez')
txt4 = '10.5'
print(txt4.isnumeric())
print()

print('----------------------------------------')
print('unicode sayılar numerik olarak düşünülür')
txt5 = '\u0030'  #unicode for 0
print(txt5.isnumeric())
print('----------------------------------------')
print()


