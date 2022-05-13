"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak başka bir listede bulunan iç içe liste öğelerini bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("\nIntersection of said nested lists:")
print(intersection_nested_lists(nums1, nums2))

