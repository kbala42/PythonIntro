print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")
bakiye = 5000

while True:
    islem = input("İşlemi seçiniz:")

    if (islem == "q"):
        print("Yine bekleriz")
        break
    elif (islem=="1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar

    elif (islem=="3"):
        miktar = int(input("Miktarı giriniz:"))

        if (bakiye-miktar<0):
            print("Böye bir miktar çekemezsiniz")
            continue
        bakiye -=miktar

