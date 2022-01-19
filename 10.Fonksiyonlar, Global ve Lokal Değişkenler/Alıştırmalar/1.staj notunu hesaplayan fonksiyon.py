print('----------------------------------------------------------tw:@tek_elo')
print('staj notunu hesaplama fonksiyonu')
print('---------------------------------------------------------------------')
print()

#sinav ve defter parametreleri ile stajNotuHesapla fonksiyonu ile tanımlıyoruz
def stajNotuHesapla(sinav,defter):
    return sinav*0.8+defter*0.2 # dönüş değerini tanımlıyoruz

# 60 ve 80 parametreleri ile fonksiyonu çağıryoruz
print("staj notu:",stajNotuHesapla(60,80))