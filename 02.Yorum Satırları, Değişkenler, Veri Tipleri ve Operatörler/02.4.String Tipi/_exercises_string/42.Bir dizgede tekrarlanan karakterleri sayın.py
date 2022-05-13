"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizgede tekrarlanan karakterleri sayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))
