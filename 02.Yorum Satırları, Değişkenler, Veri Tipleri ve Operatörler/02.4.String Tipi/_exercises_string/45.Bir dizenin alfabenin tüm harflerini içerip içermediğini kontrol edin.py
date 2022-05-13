"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizenin alfabenin tüm harflerini içerip içermediğini kontrol edin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
