"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizeyi sözlükbilimsel olarak sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))
