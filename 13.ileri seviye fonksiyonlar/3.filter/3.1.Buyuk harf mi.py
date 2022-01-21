'''
---------------------------------------------------------tw:@tek_elo
Verilen dizide bütün harfleri büyük olanları ayıran program
--------------------------------------------------------------------
'''
#Bütün harfleri büyük harf mi?
def buyukHarf(isim):
    return isim.isupper( )

#Test edilecek liste
liste=["Ali","ali","Selim","SELİM","selim"]

#buyukHarf fonksiyonu ile listeyi filtreliyoruz
sonuc=filter(buyukHarf,liste)

#Sonucu yazdırıyoruz
print(*sonuc)