sayi=45
sayac=0
print("1-100 arası bir sayı tuttum tahmin et")
while 1==1:
    sayac+=1
    cevap=int(input("1-100 arası bir sayı girin: "))
    if cevap>sayi:
        print("daha küçük bir sayı girmelisin")
    elif cevap<sayi:
        print("daha büyük bir sayı girmelisin")
    else:
        print("tebrikler tuttuğum sayıyı bildin")
        break
print("tebrikler {} seferde sayıyı bulabildin".format(sayac))