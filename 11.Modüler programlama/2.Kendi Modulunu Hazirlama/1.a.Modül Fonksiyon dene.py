print('----------------------------------------------------------tw:@tek_elo')
print('Tekrar kullanmayı düşündüğümüz kod bloklarını modüllerde saklıyoruz')
print('---------------------------------------------------------------------')
print()

# Kendi tanımladığımız modülü import ediyoruz
import modul

a = input("birinci sayıyı giriniz:")
b = input("ikinci sayıyı giriniz:")

# modul içinde bulunan toplama fonksiyonunu çağırıyoruz
sonuc = int(modul.toplama(a,b))

print(sonuc)