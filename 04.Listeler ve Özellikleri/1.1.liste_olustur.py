print('-------------------------------------------------------------@tek_elo')
print('listeler birden çok elemanı tek değişken içinde saklayan yapılardır\n'
      'Değiştirilebilir, kendi içinde sıralanabilirler')
print('---------------------------------------------------------------------')
print()

print('Boş liste oluşturma')
liste1=[]
print(type(liste1))
print(liste1)
print()

print('list() fonksiyonu ile liste oluşturma')
liste2=list()
print(type(liste2))
print(liste2)
print()

liste3=[1,2,3,4,5]
liste4=['a','b','c']
liste5=[0.5,1.7,67.89,3.14]
liste6=['ali','veli','yılmaz','hayri']
liste7=list(range(10,50,5))
print(liste7)
liste8 = list(i for i in range(1,11)) # Hesaplanan bir liste
print(liste8)
