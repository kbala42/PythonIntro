"""
-------------------------------------------------------------------tw:@tek_elo

lambda işlevini kullanarak verilen bir listeden Yok değerini kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def remove_none(nums):
    result = filter(lambda v: v is not None, nums)
    return list(result)

nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print("Original list:")
print(nums)
print("\nRemove None value from the said list:")
print(remove_none(nums))
