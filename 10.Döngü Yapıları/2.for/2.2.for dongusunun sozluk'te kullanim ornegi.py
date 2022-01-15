print('--------------------------------------------------------------tw:@tek_elo')
print(' For döngüsü ile sözlük işlemlerine genişletilmiş örnek')
print('------------------------------------------------------------------------')
print()
sayilar={"Bir":1,"İki":2,"Üç":3,"Dört":4,"Beş":5}

print("------------------------------")
print("Sözlüğün içeriği")
print("------------------------------")
print()
print(sayilar)
print()

print("------------------------------")
print("Sözlükteki anahtarlar")
print("------------------------------")
print()
for sayi in sayilar:
    print(sayi)
print()

print("------------------------------")
print("Sözlükteki değerler")
print("------------------------------")
print()
for sayi in sayilar.values():
    print(sayi)
print()

print("------------------------------")
print("Sözlükteki elemanlar")
print("------------------------------")
print()
for sayi in sayilar.items():
    print(sayi)
print()

print("-----------------------------------")
print("Sözlükteki elemanları biçimlendirme")
print("-----------------------------------")
print()
for i,j in sayilar.items():
    print("key:",i,"value:",j)
