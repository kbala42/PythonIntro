print('---------------------------------------------------------@tek_elo')
print('sozluk içinde gezinmek için döngülerden faydalanılabilir')
print('-----------------------------------------------------------------')
kisiselBilgiler={"ad":"ali",
                 "telefon":"05554442211",
                 "e_posta":"ali@abc.com",
                 "ülke":"Türkiye",
                  "il":"istanbul",
                 "ilçe":"beşiktaş"}

print('----key---')
for i in kisiselBilgiler:
    print(i)
print()

print('----value---')
for i in kisiselBilgiler:
    print(kisiselBilgiler[i])

print()

print('----key: keys() metodu ile---')
for i in kisiselBilgiler.keys():
    print(i)
print()

print('----value: values() metodu ile----')
for i in kisiselBilgiler.values():
    print(i)
print()

print('----items() metodu ile key ve value birlikte alınabilir----')
for i,j in kisiselBilgiler.items():
    print(i,j)
print()