"""
-------------------------------------------------------------------tw:@tek_elo

İlk 4 karakterde en az 2 büyük harf içeriyorsa, bir dizeyi tamamen 
büyük harfe dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))

