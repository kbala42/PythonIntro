metin3='5'
metin4='3'
print (metin3+metin4)
print(int(metin3)+int(metin4))

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

askerlikYaptiMi=True
print('Askerlik yaptı mı?', askerlikYaptiMi)
askerlikYaptiMiInt=int(askerlikYaptiMi) #integer tipine dönüştürüldü.
print('Askerlik yaptı mı?', askerlikYaptiMiInt)
askerlikYaptiMiStr=str(askerlikYaptiMi) #string tipine dönüştürüldü.
print('Askerlik yaptı mı?', askerlikYaptiMiStr)
#Çıktı olarak True verir ancak bu boolean tipinde değildir.