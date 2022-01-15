print('--------------------------------------------------------------tw:@tek_elo')
print(' Kullanıcının girdiği kullanıcı adı ve şifresini kontrol eden program')
print('-------------------------------------------------------------------------')
print()

print('--------------------------------')
print('Kullanıcı adı ve şifreyi giriniz')
print('--------------------------------')
print()

kullaniciAdi='Deneme' #Kullanıcı ad bilgisi
kullaniciParola='12345' #Kullanıcı şifresi
girisHakki=3 # Kullanıcıya verdiğimiz hak addedini saklayan değişken

while True: # sonsuz döngü

    girilenAd=input('Kullanıcı adını giriniz: ') #kullanıcının girdiği ad bilgisini saklıyoruz
    girilenParola=input('Kullanıcı parolanızı giriniz: ') #kullanıcının girdiği parola bilgisini saklıyoruz

    if kullaniciAdi==girilenAd and kullaniciParola != girilenParola:
        #Kullanıcı adı doğru ancak parola yanlışsa
        print('Kullanicı adı yada parolasını yanlış girdiniz')
        girisHakki-=1 # giriş hakkını bir azaltıyoruz

    elif kullaniciAdi!=girilenAd and kullaniciParola == girilenParola:
        # Kullanıcı adı yanlış ancak parola doğruysa
        print('Kullanicı adı yada parolasını yanlış girdiniz')
        girisHakki-=1 # giriş hakkını bir azaltıyoruz

    elif kullaniciAdi!=girilenAd and kullaniciParola != girilenParola:
        # Kullanıcı adı ve parola ikisi de yanlışsa
        print('Kullanicı adı yada parolasını yanlış girdiniz')
        girisHakki-=1 # giriş hakkını bir azaltıyoruz
    else:
        #Kullanıcı adı ve parolası doğruysa
        print('Doğru şekilde giriş yaptınız!')
        break #döngüden çık

        #Eğer giriş hakkı sıfırlanmışsa yine döngüden çıkıyoruz
    if (girisHakki ==0):
        print('Giriş hakkınız sona erdi:(')
        break