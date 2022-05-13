"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir metindeki tüm satırlardan mevcut girintiyi kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()
