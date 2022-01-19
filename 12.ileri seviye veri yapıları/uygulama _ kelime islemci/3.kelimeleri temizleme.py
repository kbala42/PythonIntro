class Dosya():

    def __init__(self):

        with open("metin.txt","r", encoding="utf-8") as file:

            dosyaIcerigi = file.read()

            kelimeler = dosyaIcerigi.split()
            self.sadeKelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")

                self.sadeKelimeler.append(i)

            for i in self.sadeKelimeler:
                print(i)


dosya = Dosya()