'''

'''

print('''
-----------------------------------------------------------------------------------------
int ve float tipinde iki değişken matematiksel işlem uygulanırsa sonuç float tipinde olur
-----------------------------------------------------------------------------------------
''')
noktaliSayi = 3.14 # Pi oktalı sayı olduğunu belirtmek için değişken adı kullandık
tamSayi = 4
alan = noktaliSayi * (tamSayi ** 2)

print('Alan: ', type(alan))
print('Dönüştürülen sayı : ', alan)

print('''
-----------------------------------------------------------------------------------------
float ve string tipinde iki değişken matematiksel işlem uygulanırsa sonuçta hata verir. 
string sayısal dönüştürülmelidir  
-----------------------------------------------------------------------------------------
''')
noktaliSayi = 3.1 # Pi oktalı sayı olduğunu belirtmek için değişken adı kullandık
stringSayi = '4'
# sonuc= noktaliSayi * stringSayi # tip hatası verir
sonuc= noktaliSayi * int(stringSayi)

print('Sonuç tipi: ', type(sonuc))
print('Sonuç sayı : ', sonuc)