'''
---------------------------------------------------------tw:@tek_elo
Bir stringte
startswith parametresindeki metin ile başlayan parça varsa true
endswith parametresindeki metin ile sonlandırılan parça varsa true
döndürür
--------------------------------------------------------------------
'''
a="Merhaba Python"
print(a.startswith("mer"))
print(a.startswith("Mer"))
print("-------------------")
print(a.endswith("HON"))
print(a.endswith("hon"))