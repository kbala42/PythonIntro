print('----------------------------------------------------------tw:@tek_elo')
print('While döngüsünü sonlandırma için harf kullanıyoruz')
print('---------------------------------------------------------------------')
liste=[]
while 1:
    ürün=input("ürün adı giriniz:")
    if ürün=="q":
        break
    liste.append(ürün)
print("girdiğiniz meyveler:",liste)

