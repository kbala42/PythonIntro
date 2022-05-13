"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir sözlükte saklanan öğrencilerin yüksekliğini ve genişliğini 
filtreleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True
nums1 = [1,2,4,6,8,10,12,14,16,17]
print ("Original list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums1)) 
nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print ("\nOriginal list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums2))
