def toplam_ve_ortalama_hesapla(n):
    toplam=0
    for i in range(n):
        toplam+=i
    ortalama=toplam/n
    print("toplam:",toplam)
    print("Ortalma:",ortalama)

toplam_ve_ortalama_hesapla(int(input("Kaça kadar sayılar hesaplamacak:")))