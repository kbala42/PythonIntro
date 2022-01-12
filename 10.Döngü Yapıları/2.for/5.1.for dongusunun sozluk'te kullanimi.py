sayilar={"Bir":1,"İki":2,"Üç":3,"Dört":4,"Beş":5}
print(sayilar)
print("------------------------------")
for sayi in sayilar:
    print(sayi)
print("------------------------------")
for sayi in sayilar.values():
    print(sayi)
print("------------------------------")
for sayi in sayilar.items():
    print(sayi)
print("------------------------------")
for i,j in sayilar.items():
    print("key:",i,"value:",j)
