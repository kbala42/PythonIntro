"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""


def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))