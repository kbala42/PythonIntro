'''
-------------------------------------------------------------------tw:@tek_elo
    endswith metodu stringin sonunda belirtilen işaretin olup olmadığını
    kontrol eder
-------------------------------------------------------------------------------
'''
print()

print('(.) nokta işaretini kontrol eder')
txt = "İsmail, şükür kavuşturana."
print(txt.endswith('.'))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.endswith(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Sonlandırılan işaret
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 
        stop                Opsiyonel. Aranılacak metnin son yeri.  
                
        ''')
print('--------------------------------------------------------')
print()

print('belirlediğimiz yerler arasında virgül arıyoruz')
print(txt.endswith(',',3,10))
print(txt.endswith(',',3,7))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Aranan stringin sonunda dizi de arayabiliriz')
print(txt.endswith('şükür kavuşturana.'))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Aranan stringin sonunda ibarede arayabiliriz')
print(txt.endswith('ana.'))
print('-----------------------------------------------------------------------')
print()