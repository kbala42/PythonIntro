liste=[i*3 for i in range(50)]

sonuc=filter(lambda x:x%2==0, liste)
print("Çift olanlar: ", *sonuc)


