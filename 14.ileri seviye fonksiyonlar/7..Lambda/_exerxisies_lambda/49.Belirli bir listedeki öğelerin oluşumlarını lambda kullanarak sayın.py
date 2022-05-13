"""
-------------------------------------------------------------------tw:@tek_elo
Belirli bir listedeki öğelerin oluşumlarını lambda kullanarak sayın
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def count_occurrences(nums):
    result = dict(map(lambda el  : (el, list(nums).count(el)), nums))
    return result
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("Original list:")
print(nums)
print("\nCount the occurrences of the items in the said list:")
print(count_occurrences(nums))

