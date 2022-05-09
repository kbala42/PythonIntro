"""
-------------------------------------------------------------------tw:@tek_elo
Girdi olarak virgülle ayrılmış sözcük dizisini kabul eden ve benzersiz
sözcükleri sıralanmış biçimde (alfanumerik olarak) yazdıran bir Python
programı yazın.
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
#items = input("Input comma separated sequence of words")
items = 'kırmızı, siyah, pembe, yeşil '
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

