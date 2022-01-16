print('''
-----------------------------------------------------------------------------tw:@tek_elo
Girilen metinde ki sesli ve sessiz harfleri farklı dizilerde saklayan program
-----------------------------------------------------------------------------------------''')
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
a=input("Bir metin giriniz:")
for i in a:
    if i in sesli_harfler:
        sesliler=sesliler+i
    if i in sessiz_harfler:
        sessizler=sessizler+i
print("sesli harfler",sesliler)
print("sessiz harfler",sessizler)