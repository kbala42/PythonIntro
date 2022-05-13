"""
-------------------------------------------------------------------tw:@tek_elo

 Belirli bir dizeden boşlukları kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("w 3 res ou r ce"))
print(remove_spaces("a b c"))
