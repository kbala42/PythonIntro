liste=[i*3 for i in range(50)]
sonuc=filter(lambda x:x>50, liste)
print(sonuc) # sonuc nesnesinin hafıza adresi
print(*sonuc)


