'''
-------------------------------------------------------------------tw:@tek_elo

    rfind metodu aranan dizinin son yerini belirler

------------------------------------------------------------------------------
'''
print()

metin = "Pireli peynirle perhizli pireler tepelerse, pireli peynirle de pır pır pervaz ederler"
print(metin.rfind('pır'))
print()

'''
------------------------------------------------------------------------------
        Syntax
                 string.rfind(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Araştırılacak değer
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 0
        stop                Opsiyonel. Aranılacak metnin sonyeri.  
                
------------------------------------------------------------------------------
'''

print()
print('-----------------------------------------------------------------------')
print(metin.rfind('pır',50,70))
print('-----------------------------------------------------------------------')
print()


print('-----------------------------------------------------------------------')
print('Aranan katar yoksa -1 döner')
print(metin.find('pır',10,20))
print('-----------------------------------------------------------------------')
print()