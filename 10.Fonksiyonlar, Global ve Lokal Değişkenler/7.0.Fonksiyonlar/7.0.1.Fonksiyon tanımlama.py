print('----------------------------------------------------------tw:@tek_elo')
print('Fonksiyon çağrıldığı zaman yürütülen kod bloklarıdır\n'
      'Böylece, kodlama içinde, defalarca aynı kod bloklarını\n'
      'tekrar tekrar yazmaya gerek kalmaz.')
print('---------------------------------------------------------------------')
print()

# Fonksiyon çağrılmadan önce yürütülecek kod bloğu ile birlikte tanımlanmalıdır
# Tanımlamayı da def anahtarsözcüğü ile yapıyoruz

# Merhaba() fonksiyonu tanımlıyoruz
def Merhaba():
    print("Merhaba")

# Hava() fonksiyonu tanımlıyoruz
def Hava():
    print("Havalar nasıl?")

#Yazdığımız yapının tipini öğreniyoruz
print(type(Merhaba))
#Yazdığımız yapının tipini öğreniyoruz
print(type(Hava))

# Merhaba() fonksiyonu çağırıyoruz
Merhaba()
# Hava() fonksiyonu çağırıyoruz
Hava()

# Merhaba fonksiyonunun adresi
print(Merhaba)
# Hava fonksiyonunun adresi
print(Hava)