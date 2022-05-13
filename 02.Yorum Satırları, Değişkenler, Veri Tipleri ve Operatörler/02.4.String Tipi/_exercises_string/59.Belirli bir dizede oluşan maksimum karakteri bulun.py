"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizede oluşan maksimum karakteri bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
 
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch

print(get_max_occuring_char("Python: Get file creation and modification date/times"))
print(get_max_occuring_char("abcdefghijkb"))
