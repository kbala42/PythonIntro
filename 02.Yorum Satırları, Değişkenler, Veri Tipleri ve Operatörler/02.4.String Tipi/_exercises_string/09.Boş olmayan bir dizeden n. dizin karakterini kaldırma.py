"""
-------------------------------------------------------------------tw:@tek_elo
Boş olmayan bir dizeden n. dizin karakterini kaldırın
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""


def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

