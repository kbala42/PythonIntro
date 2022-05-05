print('-------------------------------------------------@tek_elo')
print('key-value çiftlerini girerek')
print('--------------------------------------------------------')
sozluk= {1:"Bir",'Iki':'Iki',(3,4,5):'Samsun' }
sozluk['Yeni']='Şehir'
sozluk[(1,2)]=3+4j
sozluk[5]='Kalem'
print(sozluk.values())
print()

print('-------------------------------------')
print('update metodunu kullanarak')
print('-------------------------------------')
sozluk.update({'renk':'Turkuaz'})
print(sozluk.values())
print()

print('-------------------------------------------------@tek_elo')
print('key değeri tuple olarak atanabilir')
print('--------------------------------------------------------')
x = ('Defter',)
sozluk[x]= '40 sayfa'
print(sozluk[x])
print(sozluk)
print(sozluk[('Defter',)])
print()