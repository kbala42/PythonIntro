class Dosya():

    def __init__(self):

        with open("metin.txt","r", encoding="utf-8") as file:

            dosyaIcerigi = file.read()

            kelimeler = dosyaIcerigi.split()

            for i in kelimeler:
                print(i)

dosya = Dosya()