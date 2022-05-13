"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir dizi listesinde palindromları bulun

Bir palindromik sayı veya sayısal palindrom, rakamları ters çevrildiğinde aynı 
kalan bir sayıdır. Örneğin 16461 gibi "simetrik"tir. Palindromik terimi, 
harfleri ters çevrildiğinde yazımı değişmeyen bir kelimeye (rotor veya yarış 
arabası gibi) atıfta bulunan palindromdan türetilmiştir. İlk 30 palindromik 
sayı (ondalık olarak) şunlardır: 
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101 , 111, 
    121, 131, 141, 151, 161, 171, 181, 191, 202,...

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("\nList of palindromes:")
print(result)

