'''
---------------------------------------------------------tw:@tek_elo
map fonksiyonunun birden fazla listeye uygulanabilir.
--------------------------------------------------------------------
'''
liste1=[1,3,5]
liste2=[5,4,1]

# liste1 ve liste2 ye ikisine birden çarpma işlemi yapıyoruz
carpimListesi=list(map(lambda x,y:x*y,liste1,liste2))

print(carpimListesi)