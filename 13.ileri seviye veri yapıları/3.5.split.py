'''
---------------------------------------------------------tw:@tek_elo
split fonksiyonu stringi parametresinde verilen
şarta uygun olarak ayırır ve liste şeklinde ayırır
--------------------------------------------------------------------
'''
a="Milli Eğitim Bakanlığı"
# Boşluğa göre metni ayırıyoruz
print(a.split())
print()

a="T.B.M.M"
# noktaya göre parçalara ayırıyoruz
print(a.split("."))
print()

# alt çizgiye göre ayırıyoruz
liste="Python_Programlama_Dili".split("_")
print(liste)