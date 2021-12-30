print('---------------------------------------------------------------------')
print('---İki ifadeyi toplayabiliriz. Bu durumda çıktı yapışık olacaktır.---')
print('---------------------------------------------------------------------')
metin1 = 'Merhaba'
metin2 = 'Python'
metin3=metin1+metin2
print(metin3) #
print()

# Alternatik yazılımlar

print('---------------------------------------------------------------------')
print('---Daha düzgün toplamak için, iki metin arasına boşluk bırakıyoruz---')
print('---------------------------------------------------------------------')
# daha düzgün toplamak için
metin3=metin1+' '+ metin2
print(metin3)# Çıkışta iki kelime arasında boşuk yapmış olacağız.
print()

print('----------------------------------------------------------------------')
print('-------birinci ifadenin sonuna boşluk konabilir ----------------------')
print('----------------------------------------------------------------------')
metin1 = 'Merhaba ' #birinci ifadenin başına boşluk konabilir
metin2= 'Python'
metin3=metin1+metin2
print(metin3)
print()

print('--------------------------------------------------------------------------')
print('--------yada ikinci ifadenin başına boşluk konabilir----------------------')
print('--------------------------------------------------------------------------')
metin1 = 'Merhaba'
metin2= ' Python'
metin3=metin1+metin2
print(metin3)
print()

print('---------------------------------------------------------------------')
print('----------------Tek değişkende toplayabiliriz------------------------')
print('---------------------------------------------------------------------')
metin1 = 'Merhaba'
metin2 = 'Python'
metin1=metin1+' '+metin2
print(metin1)