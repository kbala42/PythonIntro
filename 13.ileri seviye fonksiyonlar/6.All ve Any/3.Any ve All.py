'''
---------------------------------------------------------tw:@tek_elo
Listenin tümü True'mu? all fonksiyonu kullanarak test yapma
any herhangi birisi false ise true
--------------------------------------------------------------------
'''
liste1=[True, False, True, False, False]
print(all(liste1))
print(any(liste1))
print('--------------------')
liste2=[4,-1,8,100]
print(all(liste2))

# sözlükte ise anahtalartest edilir
print('--------------------')
sozluk = {0 : "Kalem", 1 : "Defter"}
x = all(sozluk)
y = any(sozluk)
print(x)
print(y)