'''
-------------------------------------------------------------------tw:@tek_elo

    isdecimal() metodu  stringin tam sayılarda oluşup oluşmadığını
                        kontrol eder.

------------------------------------------------------------------------------
'''

txt1 = '12300'
print(txt1.isdecimal())
print()

print('--------------------------------------')
txt2 = '0012300'
print(txt2.isdecimal())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Eksi sayılar desimal olarak düşünülmez')
txt3 = '-12'
print(txt3.isdecimal())
print('--------------------------------------')
print()


print('--------------------------------------')
print('Noktalı sayılar desimal olarak düşünülmez')
txt4 = '10.5'
print(txt4.isdecimal())
print('--------------------------------------')
print()

print('----------------------------------------')
print('unicode sayılar desimal olarak düşünülür')
txt5 = '\u0030'  #unicode for 0
print(txt5.isdecimal())
print('----------------------------------------')
print()