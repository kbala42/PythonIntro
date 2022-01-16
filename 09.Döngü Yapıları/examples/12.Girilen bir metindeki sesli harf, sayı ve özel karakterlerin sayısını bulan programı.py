sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
rakamlar="1234567890"
ozel_harf=["@","!","&","?"]
ozel_harf_sayısı,rakam_sayısı,sesli_sayısı=0,0,0
kelime=input("lütfen incelemek için bir metin giriniz: ")
for harf in kelime:
    if harf in sesli_harfler:
        sesli_sayısı+=1
    if harf in rakamlar:
        rakam_sayısı+=1
    if harf in ozel_harf:
        ozel_harf_sayısı+=1
print("\ngirdiğiniz metinde {} adet sesli harf {} adet rakam ve {} adet özel karakter bulunmaktadır. ".format(sesli_sayısı,rakam_sayısı,ozel_harf_sayısı) )