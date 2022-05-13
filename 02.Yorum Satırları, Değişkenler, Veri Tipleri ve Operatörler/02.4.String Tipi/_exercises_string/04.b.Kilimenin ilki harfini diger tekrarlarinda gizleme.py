"""
-------------------------------------------------------------------tw:@tek_elo
Bir stringin ilk karakteri hariç diğer karakterlerini '*' işareti ile değiştiren program
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def change_char(str1):
  char = str1[0]
  print(char)
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

