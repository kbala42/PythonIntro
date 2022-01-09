print('---------------------------------------------------------@tek_elo')
print('update metodu veri eklemek yada value değiştirmek için kullanılır')
print('-----------------------------------------------------------------')
kisiselBilgiler={"ad":"ali","telefon":"05554442211","e_posta":"ali@abc.com","ülke":"Türkiye",
                  "il":"istanbul","ilçe":"beşiktaş"}
kisiselBilgiler.update({"e_posta":"ali77@abc.com"})
print(kisiselBilgiler.get("e_posta"))
