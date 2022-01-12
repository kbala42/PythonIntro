print("Kullanıcı adı ve şifreyi giriniz")

kullaniciAdi="Deneme"
kullaniciParola="12345"
girisHakki=3

while True:
    girilenAd=input("Kullanıcı adını giriniz: ")
    girilenParola=input("Kullanıcı parolanızı giriniz: ")

    if kullaniciAdi==girilenAd and kullaniciParola != girilenParola:
        print("Kullanicı adı yada parolasını yanlış girdiniz")
        girisHakki-=1
    elif kullaniciAdi!=girilenAd and kullaniciParola == girilenParola:
        print("Kullanicı adı yada parolasını yanlış girdiniz")
        girisHakki-=1
    elif kullaniciAdi!=girilenAd and kullaniciParola != girilenParola:
        print("Kullanicı adı yada parolasını yanlış girdiniz")
        girisHakki-=1
    else:
        print("Doğru şekilde giriş yaptınız!")
        break
    if (girisHakki ==0):
        print("Giriş hakkınız sona erdi:(")
        break