def buyukHarf(isim):
    return isim.isupper( )

liste=["Ali","ali","Selim","SELİM","selim"]

sonuc=filter(buyukHarf,liste)

print(*sonuc)