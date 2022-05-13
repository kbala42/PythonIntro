"""
-------------------------------------------------------------------tw:@tek_elo

İlk satırın girintisini ayarlayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()
