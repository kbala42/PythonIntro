print('----------------------------------------------------------tw:@tek_elo')
print('Fonksiyonunu diğer fonksiyonlar içinden de çağrılabilir')
print('---------------------------------------------------------------------')
print()

# Merhaba() fonksiyonu tanımlıyoruz
def Merhaba():
    print("Merhaba")

# Hava() fonksiyonu tanımlıyoruz
def Hava():
    print("Havalar nasıl?")

# Selamlama fonksiyonu içinden Merhaba ve Hava fonksiyonlarını çağırıyoruz
def Selamlama():
    Merhaba()
    Hava()

# Selamlama() fonksiyonu çağırıyoruz
Selamlama()

#Yazdığımız yapının tipini öğreniyoruz
print(type(Selamlama))

# Selamlama fonksiyonunun adresi
print(Selamlama)