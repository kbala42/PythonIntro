"""
-------------------------------------------------------------------tw:@tek_elo

Boşlukları belirli bir dizgenin önüne taşı

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def move_Spaces_front(str1):
  noSpaces_char = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(noSpaces_char)
  result = ' '*spaces_char
  result = '"'+result + ''.join(noSpaces_char)+'"'
  return(result)

print(move_Spaces_front("w3resource .  com  "))
print(move_Spaces_front("   w3resource.com  "))

