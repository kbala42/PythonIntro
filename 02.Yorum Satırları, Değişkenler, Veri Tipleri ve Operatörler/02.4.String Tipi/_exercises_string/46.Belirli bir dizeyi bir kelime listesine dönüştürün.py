"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizeyi bir kelime listesine dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

str1 = "The quick brown fox jumps over the lazy dog."
print(str1.split(' '))
str1 = "The-quick-brown-fox-jumps-over-the-lazy-dog."
print(str1.split('-'))
