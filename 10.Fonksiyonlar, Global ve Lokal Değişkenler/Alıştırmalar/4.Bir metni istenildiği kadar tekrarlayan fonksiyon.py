print('----------------------------------------------------------tw:@tek_elo')
print('Girilen metni istenen sayı kadar tekrarlanan fonksiyon')
print('---------------------------------------------------------------------')
print()

def Yazdir(metin, kacKere):
    for i in range  (kacKere):
        print (metin, end='\n')
        
# Fonksiyon çağırma
Yazdir('Merhaba' , 5)