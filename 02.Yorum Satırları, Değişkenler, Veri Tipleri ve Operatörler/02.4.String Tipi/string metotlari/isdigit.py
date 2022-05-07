'''
-------------------------------------------------------------------tw:@tek_elo

    isdigit() metodu  stringin sayılarda oluşup oluşmadığını
                        kontrol eder.

------------------------------------------------------------------------------
'''

txt1 = '12300'
print(txt1.isdigit())
print()

print('--------------------------------------')
txt2 = '0012300'
print(txt2.isdigit())
print('--------------------------------------')
print()

print('--------------------------------------')
print('Eksi sayılar digt olarak düşünülmez')
txt3 = '-12'
print(txt3.isdigit())
print('--------------------------------------')
print()


print('--------------------------------------')
print('Noktalı sayılar digit olarak düşünülmez')
txt4 = '10.5'
print(txt4.isdigit())
print('--------------------------------------')
print()

print('----------------------------------------')
print('unicode sayılar digit olarak düşünülür')
txt5 = '\u0030'  #unicode for 0
print(txt5.isdigit())
print('----------------------------------------')
print()