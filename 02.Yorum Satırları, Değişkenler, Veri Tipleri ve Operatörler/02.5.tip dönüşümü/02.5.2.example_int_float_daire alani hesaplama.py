piDegeri=3.14
print ('Veri Tipi: ',type(piDegeri))
#3.14 değerini verdiğimizde piDegeri float veri tipi olarak tanımlanacaktır.
yariCap=5
daireninAlani=((piDegeri*2)*yariCap)
print('Dairenin Alanı (float)=', daireninAlani)
piDegeriInt=(int(piDegeri))
# int(piDegeri*2) ifadesi float değeri int veri tipine dönüştürüldü.
print('Int veri tipine dönüştürülen piDegeri: ', piDegeriInt)
daireninAlani=((piDegeriInt*2)*yariCap)
print('Dairenin Alanı (int)=', daireninAlani)
