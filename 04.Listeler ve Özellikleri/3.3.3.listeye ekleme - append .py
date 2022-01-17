print('-------------------------------------------------------------@tek_elo')
print('listeye append metodu ile yeni elemanlar eklenebilir')
print('---------------------------------------------------------------------')
print()

list=[1,2,3,4]
list.append(5)
print(list)
print()

#list.append(6,7,8) #tek ekleme yapılabilir
#print(list)

print('append metodu ile string ekleme yapılabilir. Tek bir eleman ekleniyor kabul ediyor')
list.append('dene')
print(list)
print()

print('append metodu ile birden fazla eleman ancak tek liste verilirse eklenebilir')
list.append([10,11])
print(list)
