"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir listedeki maksimum ve minimum değerlerin tüm dizin konumlarını 
lambda kullanarak bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def position_max_min(nums):
    max_result = max(enumerate(nums), key=(lambda x: x[1]))
    min_result = min(enumerate(nums), key=(lambda x: x[1]))
    return max_result,min_result

nums = [12,33,23,10.11,67,89,45,66.7,23,12,11,10.25,54]
print("Original list:")
print(nums)
result = position_max_min(nums)
print("\nIndex position and value of the maximum value of the said list:")
print(result[0])
print("\nIndex position and value of the minimum value of the said list:")
print(result[1])
