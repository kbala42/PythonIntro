"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizgede ilk tekrarlanan kelimeyi bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("ab ca bc"))
