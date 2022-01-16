print('----------------------------------------------------------tw:@tek_elo')
print('İki boyutlu listelerle çalışma')
print('---------------------------------------------------------------------')
liste1=[(1,5),(8,2),(5,3)]
liste2=[i*j for i,j in liste1] #oluşturulan liste iç listenin elemanları çarpılarak yapılıyor
print(liste2)

print('liste2:',id(liste2))
print('--------------------')
print('liste1:',id(liste1))

