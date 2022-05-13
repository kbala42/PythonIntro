"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizenin yinelenen karakterlerini kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))

