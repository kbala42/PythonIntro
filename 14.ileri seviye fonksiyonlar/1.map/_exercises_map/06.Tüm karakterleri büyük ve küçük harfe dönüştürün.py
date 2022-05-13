"""
-------------------------------------------------------------------tw:@tek_elo

Tüm karakterleri büyük ve küçük harfe dönüştürün ve bir dizideki yinelenen 
harfleri ortadan kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))
