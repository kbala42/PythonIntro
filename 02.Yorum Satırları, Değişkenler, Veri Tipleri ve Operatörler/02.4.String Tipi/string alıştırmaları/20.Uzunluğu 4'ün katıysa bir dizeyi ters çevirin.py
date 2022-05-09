"""
-------------------------------------------------------------------tw:@tek_elo
Uzunluğu 4'ün katıysa bir dizeyi ters çevirin


-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))
