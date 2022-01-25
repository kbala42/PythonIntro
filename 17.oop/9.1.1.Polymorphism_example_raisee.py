'''
---------------------------------------------------------tw:@tek_elo
Polymorphism, aynı adlı metodun değişik nesnelerde farklı kullanımlara
sahip olmasını anlatan kavramdır
--------------------------------------------------------------------
'''
class Calisan:

	def arttir(self):
		artisOrani = 0.1
		sonuc = 100 + 100 * artisOrani
		print("Çalışan:", sonuc)

class Tekniker(Calisan):
	# arttir metodunun içeriği farklı
	def arttir(self):
		artisOrani = 0.2
		sonuc = 100 + 100 * artisOrani
		print("Çalışan:", sonuc)

class Muhendis(Calisan):
	# arttir metodunun içeriği farklı
	def arttir(self):
		artisOrani = 0.3
		sonuc = 100 + 100 * artisOrani
		print("Çalışan:", sonuc)

calisan=Calisan()

tekniker=Tekniker()

muhendis=Muhendis()

# calisanListesi adlı liste üretiyoruz
calisanListesi = [calisan, tekniker,muhendis]

#listede bütün nesnelerde arttir metodunu çalıştırıyoruz
for i in calisanListesi:
	i.arttir()