print('----------------------------------------------------------tw:@tek_elo')
print('Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu\n'
      'bulan bir fonksiyon.\n'
      'Örnek: 97 ---------> Doksan Yedi')
print('---------------------------------------------------------------------')
print()

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

def okunus(sayı):
    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci] + " " + birler[birinci]


sayi = int(input("Sayı:"))

print(okunus(sayi))