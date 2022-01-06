'''

'''

print('----------------------------------------------------\n'
      'Tam sayı değişkenden noktalı sayı değişkene dönüşüm\n' 
      '----------------------------------------------------\n')
tamSayi = 5
print('Dönüşen sayı tipi: ', type(tamSayi))
print('Dönüşen sayı : ', tamSayi)
noktaliSayi = float(tamSayi)
print('Dönüştürülen sayı tipi: ', type(noktaliSayi))
print('Dönüştürülen sayı: ', noktaliSayi)


print('''
--------------------------------------------------
Noktalı sayı değişkenden tam sayı değişkene dönüşüm
--------------------------------------------------
''')
noktaliSayi = 3.14
print('Dönüşen sayı tipi: ', type(noktaliSayi))
print('Dönüşen sayı : ', noktaliSayi)
tamSayi = int(noktaliSayi)
print('Dönüştürülen sayı tipi: ', type(tamSayi))
print('Dönüştürülen sayı : ', tamSayi)

print('''
----------------------------------------------------------
Metin sayı (rakam) değişkenden tam sayı değişkene dönüşüm
----------------------------------------------------------
''')
metinSayi='250'
print('Dönüşen sayı tipi: ', type(metinSayi))
print('Dönüşen sayı : ', metinSayi)
tamSayi = int(metinSayi)
print('Dönüştürülen sayı tipi: ', type(tamSayi))
print('Dönüştürülen sayı : ', tamSayi)

print('''
----------------------------------------------------------
Metin sayı (rakam) değişkenden noktalı sayı değişkene dönüşüm
----------------------------------------------------------
''')
metinSayi='3.14'
print('Dönüşen sayı tipi: ', type(metinSayi))
print('Dönüşen sayı : ', metinSayi)
noktaliSayi = float(metinSayi)
print('Dönüştürülen sayı tipi: ', type(noktaliSayi))
print('Dönüştürülen sayı : ', noktaliSayi)
print('')
print('Eğer Noktalı bir rakamı, tam sayı değişkene dönüştürseydik:')
print('')
tamSayi = float(metinSayi)
print('Dönüştürülen sayı tipi: ', type(tamSayi))
print('Dönüştürülen sayı : ', tamSayi)
print('')
print('hata vermeyecek ama çıkış alamıyacaktık')

print('''
----------------------------------------------------------
Metini tam sayıya dönüştürürsek hata alacağız
----------------------------------------------------------
''')
metinMetin = 'Yalova'
#print(int(metinMetin))


print('''
-----------------------------------------------------------------------------------------
İki rakamı toplarsak iki metnin toplamı gibi olur. Yani çıkışta rakamlar yan yana yazılır
-----------------------------------------------------------------------------------------
''')
metinBir = '50'
metinIki = '30'
print(metinBir+metinIki)
print('''
-----------------------------------------------------------------------------------------
İki rakamı toplamak için önce int yada float'ta dönüştürülüp toplama yapılır
-----------------------------------------------------------------------------------------
''')
print(int(metinBir)+int(metinIki))

print('''
-----------------------------------------------------------------------------------------
Kullanıcı giriş yapılırsa giriş metin olduğu için matematiksel işlemlerde int yada float
değişkeni dönüştürülmelidir
-----------------------------------------------------------------------------------------
''')
# rakam=input('Bir sayi giriniz:') # örneğin 15
# print('Dönüşen sayı tipi: ', type(rakam))
# print('Dönüşen sayı : ', rakam)
# tamSayi = int(rakam)
# print('Dönüştürülen sayı tipi: ', type(tamSayi))
# print('Dönüştürülen sayı : ', tamSayi)


