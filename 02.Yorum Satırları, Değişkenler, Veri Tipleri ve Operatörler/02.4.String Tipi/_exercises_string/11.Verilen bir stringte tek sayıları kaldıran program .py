"""
-------------------------------------------------------------------tw:@tek_elo

Verilen bir stringte tek sayıları kaldıran bir program yazınız

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def strCiftDegerler(mtn):
  sonuc = ""
  for i in range(len(mtn)):
    if i % 2 == 0:
      sonuc = sonuc + mtn[i]
  return sonuc

print(strCiftDegerler('abcdef'))
print(strCiftDegerler('python'))
