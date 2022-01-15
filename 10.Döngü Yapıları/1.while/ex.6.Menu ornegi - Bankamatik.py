print('--------------------------------------------------------------tw:@tek_elo')
print(' Bankamatik menüsü programı')
print('------------------------------------------------------------------------')
print()
print("********************\nATM sistemine hoşgeldiniz\n********************")

print('''
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

''')
bakiye = 5000

while True: # sonsuz döngüyü başlatıyoruz

    islem = input("İşlemi seçiniz:") # Kullanıcının isteğini saklıyoruz

    if (islem == "q"): # kullanıcı çıkış istemişse
        print("Yine bekleriz")
        break

    elif (islem=="1"): # kullanıcı bakiye istemişse
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"): # kullanıcı para yatırmayı istemişse
        miktar = int(input("Miktarı giriniz:")) # yatıracağı para miktarını saklıyoruz
        bakiye += miktar # girilen miktarı önceki bakiye ile toplayıp yeni bakiyeyi buluyoruz

    elif (islem=="3"):# kullanıcı para çekmekistemişse
        miktar = int(input("Miktarı giriniz:"))# çekeceği para miktarını saklıyoruz

        if (bakiye-miktar<0): # istenen para bakiyeden büyükse
            print("Böye bir miktar çekemezsiniz")
            continue # mesajı yazdıktan sonra devam etmesini sağlıyoruz
        bakiye -=miktar

