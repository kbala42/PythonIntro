"""
-------------------------------------------------------------------tw:@tek_elo
Her sayının içerdiği her basamağa bölünebildiği belirli bir aralıktaki 
sayıları bulun


-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))
