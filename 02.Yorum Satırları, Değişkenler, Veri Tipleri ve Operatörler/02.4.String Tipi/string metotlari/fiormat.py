'''
-------------------------------------------------------------------tw:@tek_elo
    format metodu belirlenen formatı, konumlandığı yere uygular
-------------------------------------------------------------------------------
'''
txt = '1 radyan {x:.2f} derece eder'
print(txt.format(x = 52))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.format(value1, value2...)

        Parametre	        Tanım
        value1, value2      Zorunlu. Dizeye biçimlendirilmesi ve eklenmesi gereken bir veya daha fazla değer.
                            Değerler, virgülle ayrılmış bir değerler listesi, bir anahtar=değer listesi veya 
                            her ikisinin birleşimidir. Değerler herhangi bir veri türünden olabilir.
 

        ''')
print('--------------------------------------------------------')

print('-----------------------------------------------------------------------')
print('Değerler adlandırılmış dizinler şeklinde olabilir')
txt = '{ad} ilimiz {bolge} bölgesinde yer almaktadır'
print(txt.format(ad = 'Yalova', bolge = 'Marmara'))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Değerler indislerle verilebilir')
txt = '{0} ilimiz {1} bölgesinde yer almaktadır'
print(txt.format('Yalova', 'Marmara'))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Değerler boş olarak verilirse sıra ile yerleştirilir')
txt = '{} ilimiz {} bölgesinde yer almaktadır'
print(txt.format('Yalova', 'Marmara'))
print('-----------------------------------------------------------------------')
print()