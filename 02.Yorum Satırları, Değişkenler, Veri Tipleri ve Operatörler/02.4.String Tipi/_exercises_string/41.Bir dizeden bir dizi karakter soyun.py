"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizeden bir dizi karakter soyun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print("\nOriginal String: ")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")      
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
print()
