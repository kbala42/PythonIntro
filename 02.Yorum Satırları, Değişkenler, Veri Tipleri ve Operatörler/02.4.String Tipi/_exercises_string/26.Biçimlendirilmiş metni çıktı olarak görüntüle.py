"""
-------------------------------------------------------------------tw:@tek_elo

Biçimlendirilmiş metni çıktı olarak görüntüle

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
print()
print(textwrap.fill(sample_text, width=50))
print()

