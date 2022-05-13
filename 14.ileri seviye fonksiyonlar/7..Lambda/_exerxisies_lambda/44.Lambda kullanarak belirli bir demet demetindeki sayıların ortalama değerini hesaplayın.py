"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir demet demetindeki sayıların ortalama değerini hesaplayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result

nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))
