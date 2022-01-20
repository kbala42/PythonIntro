'''
---------------------------------------------------------tw:@tek_elo
map fonksiyonunu farklı sayıda listelere uygulandığında
yalnızca ortak indise sahip olanlara yygulanır
--------------------------------------------------------------------
'''
liste1=[1,3,5]
liste2=[5,4,1]
liste3=[6,1,9,10,15,20]

carpimListesi=list(map(lambda x,y,z:x*y*z,liste1,liste2,liste3))
print(carpimListesi)