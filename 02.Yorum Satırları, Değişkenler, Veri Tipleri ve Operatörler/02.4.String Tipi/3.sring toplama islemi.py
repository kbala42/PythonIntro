metin1 = 'Merhaba'
metin2 = 'Python'
metin3=metin1+metin2
print(metin3) #iki ifadeyi toplayabiliriz
print('------daha düzgün toplamak için------------------------')
# daha düzgün toplamak için
metin3=metin1+' '+ metin2
print(metin3)
print('-------birinci ifadenin başına boşluk konabilir ----------------------')
# yada
metin1 = 'Merhaba ' #birinci ifadenin başına boşluk konabilir
metin2= 'Python'
metin3=metin1+metin2
print(metin3)
print('--------yada ikinci ifadenin başına boşluk konabilir----------------------')
metin1 = 'Merhaba'
metin2= ' Python'
metin3=metin1+metin2
print(metin3)
print('----------Tek değişkende toplayabiliriz-----------------')
metin1 = 'Merhaba'
metin2 = 'Python'
metin1=metin1+' '+metin2
print(metin1)