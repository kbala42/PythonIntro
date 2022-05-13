"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir dizeler listesindeki bir dizenin tüm 
anagramlarını bulun

bir anagram, tüm orijinal harfleri tam olarak bir kez kullanarak yeni bir 
kelime veya ifade üretmek için bir kelimenin veya ifadenin harflerini yeniden 
düzenlemenin sonucu olan doğrudan kelime değiştirme veya kelime oyunudur; 
örneğin, anagram kelimesi nag-a-ram olarak yeniden düzenlenebilir.
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)

