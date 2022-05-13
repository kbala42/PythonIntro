"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizede ilk tekrarlanan karakteri bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c 
  return "None"

print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))
