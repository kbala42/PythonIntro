print('--------------------------------------------------------')
print('index metodu aranan değerin ilk yerini belirler')
print()
print('Bulamazsa bir istisna(exception) oluşturur')
print()
print('find metodu ile farkı, find -1 döndürür')
print('--------------------------------------------------------')
metin = "İsmail, şükür kavuşturana"
print(metin.index('şü'))
print()

print('--------------------------------------------------------')
print(''' Syntax
                 string.index(value, start, end)
                 
        Parametre	        Tanım
        value	            Zorunlu. Araştırılacak değer
        start	            Opsiyonel. Aranılacak metnin başlangıç yeri. Varsayım 9
        stop                Opsiyonel. Aranılacak metnin sonyeri.  
                
        ''')
print('--------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')
print(metin.index('il',3,10))
print('-----------------------------------------------------------------------')
print()


print('-----------------------------------------------------------------------')
print('Aranan katar yoksa exception döner')
#print(metin.index('5',3,10))
print('-----------------------------------------------------------------------')
print()