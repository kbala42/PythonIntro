'''
-------------------------------------------------------------------tw:@tek_elo
    rindex metodu aranan değerin son yerini belirler

    Bulamazsa bir istisna(exception) oluşturur

    rfind metodu ile farkı, find -1 döndürür
------------------------------------------------------------------------------
'''

metin = " Çarşıda koza ucuz, çarşıda darı ucuz, çarşıda boza da ucuz mu?"
print(metin.index('ucuz'))
print()

'''
------------------------------------------------------------------------------
        Syntax
                 string.rindex(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Araştırılacak değer
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 0
        stop                Opsiyonel. Aranılacak metnin sonyeri. 
------------------------------------------------------------------------------
'''
print('-----------------------------------------------------------------------')
print(metin.rindex('ucuz',10,20))
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Aranan katar yoksa exception döner')
#print(metin.rindex('ucuz',3,10))
print('-----------------------------------------------------------------------')
print()