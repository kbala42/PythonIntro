'''
-------------------------------------------------------------------tw:@tek_elo
    
    starswith metodu stringin belirlenen değerle başlayıp 
    başlamadığını kontrol eder
    
-------------------------------------------------------------------------------
'''
print()

txt = "İsmail, şükür kavuşturana."
print(txt.startswith('İsmail'))
print()

'''
------------------------------------------------------------------
     Syntax
     
             string.startswith(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Sonlandırılan işaret
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 
        stop                Opsiyonel. Aranılacak metnin son yeri.  
                
    
-------------------------------------------------------------------------------
'''
print()

print('belirlediğimiz yerler arasında değeri test ediyoruz')
print(txt.startswith('şü',8,10))
print(txt.startswith('Şü',8,10))
print('-----------------------------------------------------------------------')
print()

