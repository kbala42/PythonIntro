"""
-------------------------------------------------------------------tw:@tek_elo

İlk oluşum indeksinin en küçük olduğu belirli bir dizgenin ilk tekrarlanan karakterini bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def first_repeated_char_smallest_distance(str1):
  temp = {}
  for ch in str1:
    if ch in temp:
      return ch, str1.index(ch);
    else:
      temp[ch] = 0
  return 'None'
print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))
