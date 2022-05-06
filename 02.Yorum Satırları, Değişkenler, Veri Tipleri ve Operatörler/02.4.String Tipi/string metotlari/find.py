'''
-------------------------------------------------------------------tw:@tek_elo
print('find metodu aranan dizinin yerini belirler')
-------------------------------------------------------------------------------
'''
print()

metin = "İsmail, şükür kavuşturana"
print(metin.find('şü'))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.find(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Araştırılacak değer
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 9
        stop                Opsiyonel. Aranılacak metnin sonyeri.  
                
        ''')
print('--------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')
print(metin.find('il',3,10))
print('-----------------------------------------------------------------------')
print()


print('-----------------------------------------------------------------------')
print('Aranan katar yoksa -1 döner')
print(metin.find('ara',3,10))
print('-----------------------------------------------------------------------')
print()