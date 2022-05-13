"""
-------------------------------------------------------------------tw:@tek_elo

map ve lambda kullanarak verilen iki listeyi eklemek için programı yazın.

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("Original list:")
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))

